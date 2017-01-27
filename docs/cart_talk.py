"""Source code used for the talk:
http://www.slideshare.net/MarcGarcia11/cart-not-only-classification-and-regression-trees
"""

# data

import pandas as pd

data = {'age': [38, 49, 27, 19, 54, 29, 19, 42, 34, 64,
                19, 62, 27, 77, 55, 41, 56, 32, 59, 35],
        'distance': [6169.98, 7598.87, 3276.07, 1570.43, 951.76, 139.97, 4476.89,
                     8958.77, 1336.44, 6138.85, 2298.68, 1167.92, 676.30, 736.85,
                     1326.52, 712.13, 3083.07, 1382.64, 2267.55, 2844.18],
        'attended': [False, False, False, True, True, True, False, True, True, True,
                     False, True, True, True, False, True, True, True, True, False]}

df = pd.DataFrame(data)


# base_plot

from bokeh.plotting import figure, show

def base_plot(df):
    p = figure(title='Event attendance',
               plot_width=900,
               plot_height=400)
    p.xaxis.axis_label = 'Distance'
    p.yaxis.axis_label = 'Age'
    p.circle(df[df.attended]['distance'],
             df[df.attended]['age'],
             color='red',
             legend='Attended',
             fill_alpha=0.2,
             size=10)
    p.circle(df[~df.attended]['distance'],
             df[~df.attended]['age'],
             color='blue',
             legend="Didn't attend",
             fill_alpha=0.2,
             size=10)
    return p

_ = show(base_plot())


# tree_to_nodes

from collections import namedtuple
from itertools import starmap

def tree_to_nodes(dtree):
    nodes = starmap(namedtuple('Node', 'feature,threshold,left,right'),
                    zip(map(lambda x: {0: 'age', 1: 'distance'}.get(x),
                            dtree.tree_.feature),
                        dtree.tree_.threshold,
                        dtree.tree_.children_left,
                        dtree.tree_.children_right))
    return list(nodes)


# cart_plot

from collections import namedtuple, deque
from functools import partial

class NodeRanges(namedtuple('NodeRanges', 'node,max_x,min_x,max_y,min_y')):
    pass

def cart_plot(df, dtree, nodes, limit=None):
    nodes = tree_to_nodes(dtree)

    plot = base_plot()
    add_line = partial(plot.line, line_color='black', line_width=2)

    stack = deque()
    stack.append(NodeRanges(node=nodes[0],
                            max_x=df['distance'].max(),
                            min_x=df['distance'].min(),
                            max_y=df['age'].max(),
                            min_y=df['age'].min()))

    count = 1
    while len(stack):
        node, max_x, min_x, max_y, min_y = stack.pop()
        feature, threshold, left, right = node

        if feature == 'distance':
            add_line(x=[threshold, threshold],
                     y=[min_y, max_y])

        elif feature == 'age':
            add_line(x=[min_x, max_x],
                     y=[threshold, threshold])

        else:
            continue

        stack.append(NodeRanges(node=nodes[left],
                                max_x=threshold if feature == 'distance' else max_x,
                                min_x=min_x,
                                max_y=threshold if feature == 'age' else max_y,
                                min_y=min_y))

        stack.append(NodeRanges(node=nodes[right],
                                max_x=max_x,
                                min_x=threshold if feature == 'distance' else min_x,
                                max_y=max_y,
                                min_y=threshold if feature == 'age' else min_y))

        if limit is not None and count >= limit:
            break
        else:
            count += 1

    show(plot)


# decision_tree_model

def decision_tree_model(age, distance):
    if distance >= 2283.11:
        if age >= 40.00:
            if distance >= 6868.86:
                if distance >= 8278.82:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
    else:
        if age >= 54.50:
            if age >= 57.00:
                return True
            else:
                return False
        else:
            return True


# entropy

import math

def entropy(a, b):
    total = a + b
    prob_a = a / total
    prob_b = b / total
    return - prob_a * math.log(prob_a, 2) - prob_b * math.log(prob_b, 2)


# get_best_split

def get_best_split(x, y):
    best_split = None
    best_entropy = 1.
    for feature in x.columns.values:
        column = x[feature]
        for value in column.iterrows():
            a = y[column < value] == class_a_value
            b = y[column < value] == class_b_value
            left_weight = (a + b) / len(y.index)
            left_entropy = entropy(a, b)

            a = y[column >= value] == class_a_value
            b = y[column >= value] == class_b_value
            right_weight = (a + b) / len(y.index)
            right_entropy = entropy(a, b)

            split_entropy = left_weight * left_entropy + right_weight * right_entropy
            if split_entropy < best_entropy:
                best_split = (feature, value)
                best_entropy = split_entropy

    return best_split


# train_decision_tree

def train_decision_tree(x, y):
    feature, value = get_best_split(x, y)

    x_left, y_left = x[x[feature] < value], y[x[feature] < value]
    if len(y_left.unique()) > 1:
        left_node = train_decision_tree(x_left, y_left)
    else:
        left_node = None

    x_right, y_right = x[x[feature] >= value], y[x[feature] >= value]
    if len(y_right.unique()) > 1:
        right_node = train_decision_tree(x_right, y_right)
    else:
        right_node = None

    return (feature, value, left_node, right_node)

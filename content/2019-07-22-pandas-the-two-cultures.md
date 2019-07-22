Title: pandas: The two cultures
Author: Marc
Date: 2019-07-22 23:26:00
Slug: pandas-the-two-cultures
Tags: pandas

# pandas: The two cultures

![](/static/img/blog/two_cultures/leo_breiman.jpeg)

In 2001, [Leo Breiman](https://www.stat.berkeley.edu/~breiman/) published the
paper [Statistical Modeling: The Two Cultures](http://www2.math.uu.se/~thulin/mm/breiman.pdf).
Breiman was a distinguished statistician at UC Berkeley, known among other things for his
major contributions to CART (decision trees), and ensemble techniques, mainly bootstrap
aggregation. Combining both, he was able to define one of the most popular machine learning
models even today (18 years after the publication of the paper)
[Random forests](https://www.stat.berkeley.edu/~breiman/randomforest2001.pdf).

In the paper of about _The two cultures_, Breiman identified that there were two somehow
conflicting cultures in the discipline of statistical modeling. One that was focussing on
modelling (and trying to understand) the stochastic process generating some data. While the
other followed an algorithmic approach focussed on obtaining results (minimizing the error
between the model results and the data), and considered the stochastic process a black box.
Today the division is clear, and in a way, machine learning is not even considered part of
statistics. While this may or may not be a good thing, identifying in 2001 that both
communities were different and had different needs, surely helped overcome the frustration
of the machine learning community at that time, and sped up its development. Today, publishing
papers in machine learning, and specifically in the area of neural networks, is mostly driven by 
the obtained results, more than by the theory behind the results. Ali Rahimi gave
[his view](https://www.youtube.com/watch?v=Qi1Yry33TQE) when receiving the test-of-time award
at NeurIPS 2017.

But this post is not about machine learning, but about [pandas](https://pandas.pydata.org/).
And about the two cultures in the pandas community, that I don't think are often well identified,
causing frustration to the users, and making decision making difficult to developers.

## Dr Jekyll and Mr Hyde

For the last years I've been mainly working as a data scientist. Since the developers of
[scikit-learn](https://scikit-learn.org/stable/) are doing all the _fun_ work and implementing
all the complex algorithms for the rest of us, I'll argue that my job (and the job of the rest
of data scientists, who will probably disagree) is to work on data analysis to find out what
I want to do, and data engineering to make it work in production.

What I call **data analysis** here is performed in a [Jupyter notebook](https://jupyter.org/),
where I analyze and visualize the data, I found out what is wrong with the data, and I quickly
grow the cells of my ``Untitled23.ipynb`` hoping I'll never have to look back at my dirty code.
What I value the most is being able to write code fast, to the extend I alias every Python
library I import to things like ``np``, ``pd``, ``plt`` to make sure I save those microseconds
from typing the actual names the developers of those tools decided. And I really appreciate
the software making as many decisions as needed to save me from having to spend the time on
being explicit on what I want. Ok, this is a bit exagerated, and I don't really let my notebook
names be untitled whatever, or use aliases, but I think you see my point.

On the other hand, when working in **data engineering** I use vim, and I write all my code in
Python files in a clear directory structure. Every file and directory are carefully named,
every function is documented, and the best coding standards are applied. All my code is versioned
controlled with git, and code reviewed by my colleagues. I write every single line of code knowing
that I will have to revisit it many times, and I optimize for its simplicity and its clarity.
The thing I'm more adverse to is to _magic_, and software making decisions for me. I want to be
in control, I want everything in my code to be deterministic, and I want everything in my code
to be explicit. Everything that Tim Peters wrote in [PEP-20](https://www.python.org/dev/peps/pep-0020/),
the Zen of Python, applies:

- Beautiful is better than ugly.
- Explicit is better than implicit.
- Simple is better than complex.
- Readability counts.
- Errors should never pass silently.
- ...

## One pandas to rule them all

![](/static/img/blog/two_cultures/ring.jpeg)

What I find the most interesting part about _The two cultures_ I just described, is that I use
pandas for both. I think pandas is the best tool for both use cases, and I won't admit I'm biased
here, since I'm a pandas maintainer because I use the software, and not the other way round.

But how is that possible? Both use cases are radically different. Is pandas designed in a way that
can offer an API to both kinds of users what they need? Is that always possible.

Let's find the answer with examples.

## Show me the code

### Creating data from a Python dict

Let's start with a single example, by manually creating some data:

```python
>>> import pandas

>>> num_legs = pandas.Series({'unicorn': 4, 'spider': 8, 'penguin': 2})
>>> num_legs
unicorn    4
spider     8
penguin    2
dtype: int64
```

I think we can agree that pandas is letting us create our data in the simplest possible way. There
are other options that pandas lets us do, like providing one list for the values and another for the
index too, which in some cases can be more convenint. As a data analyst, I don't think pandas can
be improved to make our life easier.

But as a data engineering, there are more things to consider. Imagine our data, instead of having 3
samples, has 3 million. How much memory is pandas consuming here? And why? For simplicity, let's
consider only the values (and not the name of the animals):

```python
>>> num_legs.memory_usage(index=False)
24
```

The values in our Series are consuming 24 bytes. If we see again the representation of our Series,
we can see how the data type (aka dtype) is ``int64``. Meaning that every value will consume 64
bits (8 bytes). 8 bytes per value, multiplied by 3 values (the number of legs for unicorn, spider
and penguin) totals 24 bytes. But why 64 bits? pandas decided for us that representation, which can
store numbers from around -9e18 to 9e18. But do we really expect animals to have a number of legs
with 18 digits? Or do we expect negative numbers of legs at all? Probably not. We know it, but
pandas don't, and it's deciding for us a conservative representation for our data that won't
cause as problems (as opposed as one that saves as memory).

In this case, the Series constructor has a paramter ``dtype`` that we can use to tell pandas to not
decide for us how to internally represent the data, but to tell it explicitly. This is the result:

```python
>>> import pandas

>>> num_legs = pandas.Series({'unicorn': 4, 'spider': 8, 'penguin': 2},
...                          dtype='uint8')
>>> num_legs
unicorn    4
spider     8
penguin    2
dtype: uint8

>>> num_legs.memory_usage(index=False)
3
```

In this case, I think we can conclude that pandas is serving well our two kind of users. For users
who want fast results and may not know about internals of computers or data types, pandas serves them
well but making a reasonable decision, that will work well at the cost of higher memory consumption,
which most users won't see as a problem. For the users writing production systems, where memory can
be a bottleneck, they are able to avoid pandas making assumptions, and will be able to use the
memory they need at the cost of providing an addition parameter.

### How many legs unicorns have?

![](/static/img/blog/two_cultures/unicorn.jpeg)

An important question we face is, how many legs unicorns have? In the previous example, we specified
they have 4, but do unicorns really have 4 legs? Does anybody has seen a unicorn? Let's try to be
prudent and say that we don't know. By convention, when we have an unknown or missing value, we
represent it as ``NaN`` (Not a Number). ``NaN`` is represented internally as a sequence of bits
reserved to have the meaning of ``NaN`` instead of the numeric value that the floating point
representation would mean. If that sounds too complex, think that in binay, ``0000`` can represent
the number 0, ``0001`` the 1, ``0010``: 2, ``0011``: 3... and ``1111``: 15. And what microprocessors
manufacturers decided is something like letting represent only from 0 to 14 (instead of from 0 to 15
that we can with 4 bits), and reserve the ``1111`` to mean ``NaN``. Things are in reality more complex,
since ``NaN`` representations only exists for floating points numbers (aka float), which are decimals,
and also, other special values like ``Inf`` or ``-Inf``` exists. But that explanation gives an idea.

So, back to the example, if we want to represent that we don't know how many legs unicorns have, we
can simply do:

```python
>>> num_legs.loc['unicorn'] = float('NaN')
>>> num_legs
unicorn    NaN
spider     8.0
penguin    2.0
dtype: float64
```

Many things happened here. We can see, how besides the expected change, having ``NaN`` unicorn legs,
now we are back to consuming 64 bits, and not only, but also the rest of values in the column now are
decimal (float) values. As I just explained, and can also be seen in the example, ``NaN`` is a float
value. Modern computers don't have an integer representation for ``NaN``, so for pandas to do what we
asked it to do, converting the column to float was the _only_ option (not really the only, but let's
pretend for a second).

It feels a bit wierd to see in the Series representation that a penguin has 2.0 legs. It's conceptually
wrong, and also misleading making us belive that animals can have a decimal number of legs. There are
also performance implications, we are consuming 4 times more memory now, and also operations among
integers don't take the same time as operations among floats (note that while floats are a more complex
representation, modern CPUs are highly optimised for them, and operations can even be faster for floats
than for ints).

But there is something else, see this example:

```python
>>> 0.1 + 0.2 == 0.3
False
```

Floatting point numbers are approximation. They are mapping an infinite set of numbers (let's say all
real numbers) to the finite set of possible representations with 64 bits (``2 ** 64``). While in many
cases using this approximate values won't make a difference (the height of a person keeps being the
same if we change the 20th decimal), if our column encoded an id we are planning to use to join with
another data source later, we can experience data loss and bugs with the automatic type cast pandas
just did.

In pandas 0.24 we introduced a new data type to mix integer values with missing values. This is done
by instead of using the float ``NaN`` to represent the missing values, we internally keep a separate
boolean array that identifies where the missing values are. This adds an extra layer of complexity
into pandas, but avoids problems like the one just described. By default, pandas still uses the
original types, but we can write the previous code as follows:

```python
>>> num_legs = pandas.Series({'unicorn': 4, 'spider': 8, 'penguin': 2},
...                          dtype='UInt8')
>>> num_legs.loc['unicorn'] = float('NaN')
>>> num_legs
unicorn    NaN
spider       8
penguin      2
dtype: UInt8
```

Note that ``UInt8`` represents the pandas type with the mask, and ``uint8`` (lowercase) represents the
original type based on numpy. Also note that the new type may not be as stable as the old, and may not
implement all the operations.

While the new data type fixes this specific problem, the fact that pandas silently casts a data type
when needed is very convinient for the use cases of data analysts, but in my opinion does a poor job
to the interests of precision and reliability of data engineers. And the ``.loc[]`` syntax is very
convenient, but doesn't allow us to solve the problem with a simple parameter. A new
[pandas option](https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html) could possibly
be the best option to control this behavior of pandas, and make it raise an exception when an operation
is not possible without casting.

The most popular pandas function
--------------------------------

CSV is in general a poor format to store data. It has clearly a great advantage, that is being able
to open CSV files in a text editor. Other than that, all are disadvantages:

- Inefficient storage (space that file uses in disk)
- Inefficient I/O (because the volume of data, and also the required casting)
- Lack of types (everything is a string in a CSV)
- Lack of a standard (different quoting, delimiters,...)

Despite of those, CSV happens to be one of the most popular formats out there, being the
documentation of ``pandas.read_csv`` the one with most visits in the pandas documentation.

To manage all the trickiness of the format, ``pandas.read_csv`` provides as much as 50
arguments, to customize for your file format, and for your needs.
[static-frame](https://github.com/InvestmentSystems/static-frame) a project (somehow)
aiming to compete with pandas, contains the next sentence in its README file:

> The Pandas CSV reader far out-performs the NumPy-based reader in StaticFrame: thus, for now, using Frame.from_pandas(pd.read_csv(fp)) is recommended for loading CSV files.

This gives an idea of all the complexity in the CSV parser, not only in terms of the parameters,
but also in terms of how optimized it is for performance.

Despite being one of the most powerful and optimized CSV parsers out there,
[James Powell](http://twitter.com/dontusethiscode) gave a
[lightning talk at PyData London 2019](https://www.youtube.com/watch?v=QkQ5HHEu1b4&t=1554)
on how the parser could be easily improved in several ways for his needs.

Those include:

- Assume string columns are properly encoded and load them directly into memory
- Optimize date casting by assuming a specific format, and a limited set of values

Again, no matter the great job done in implementing pandas, the software is
being unable to fully satisfy all user cases. ``pandas.read_csv`` does again a
good job at making life easy to data analysts (as defined at the beginning of this
post). And it also does an impressive job at adding parameters to empower users that
know what they are doing and have production-ready code need (data engineers). But
even with an insane number of parameters like 50, looks like loading a CSV file into
memory is too complex for a generic function.

What is the solution here? Personally, I think that _one pandas t0 rule them all_
is possible and still the best option. But not a ``pandas.read_csv`` to rule them all.
My view is that pandas shouldn't have I/O modules that are able to load data from
every format, and do it in a way that solves every user needs. That's just impossible.
But pandas could do a better job at allowing and encouraging an ecosystem of I/O
pandas plugins. I proposed in [this ticket](https://github.com/pandas-dev/pandas/issues/26804)
a first refactoring that would make this possible, which is still under discussion.
I'll write in a different article more details about this proposal.

Lazy pandas
-----------

![](/static/img/blog/two_cultures/lazy_pandas.jpeg)

To conclude this article, I will talk about what in my opinion is one of the biggest
differences between the needs of data analysts using pandas in a Jupyter notebook,
compared to the data engineers using it to write production pipelines.

See this example:

```python
>>> num_legs = pandas.Series({'unicorn': 4, 'spider': 8, 'penguin': 2})
>>> num_legs.median()
4.0

>>> num_legs = num_legs.to_frame()
>>> num_legs
         0
unicorn  4
spider   8
penguin  2

>>> num_legs = num_legs.rename(columns={0: 'legs'})
>>> num_legs
         legs
unicorn     4
spider      8
penguin     2

>>> num_legs['kind'] = num_legs['legs'].replace({2: 'biped',
...                                              4: 'quadruped',
...                                              8: 'octoped'})
>>> num_legs
         legs       kind
unicorn     4  quadruped
spider      8    octoped
penguin     2      biped

>>> num_legs = num_legs[num_legs.legs <= 4]
         legs       kind
unicorn     4  quadruped
penguin     2      biped

>>> num_legs.to_parquet('num_legs.parquet')
```

And compare it with this other code:

```python
>>> (pandas.Series({'unicorn': 4, 'spider': 8, 'penguin': 2})
...        .to_frame()
...        .rename(columns={0: 'legs'})
...        .assign(kind=lambda df: df['legs'].replace({2: 'biped',
...                                                    4: 'quadruped',
...                                                    8: 'octoped'}))
...        .query('legs <= 4')
...        .to_parquet('num_legs.parquet'))
```

Before you are tempted to think on which one is better, let's discuss which
problem solves each of them.

The first version is part of an iterative process where at every step we need
to visualize how or data looks like. We also may need not only to visualize the
data, but _understand_ or verify it, for example by checking which is the mean
of the column. It is likely that at the end of writing that code, we don't care
about it anymore, since we already extracted the insights we care about.

But the second case, while doing almost the same, is code written to be read
and to be maintained. If there is a bug in the code, it should be easy to
understand what it does, and fix it. The goal is not to discover anything
while writting the code, just to add a functionality to a system, and to be
able to run it in a reliable and performant way.

For more information about the style in the second approach, you can check
the must-read [Method Chaining](https://tomaugspurger.github.io/method-chaining)
by the pandas maintainer [Tom Augspurger](https://tomaugspurger.github.io/pages/about.html).
Also, I discussed about method chaining in my talk
[Towards pandas 1.0](https://www.youtube.com/watch?v=hK6o_TDXXN8).

Back to the example, pandas let us write code in a way that suits both
data analysts and data engineers. But there is something else that is worth
considering. In the first version, the operations must be executed one at
a time, since they are independent. But in the example using method chaining,
there is no need to execute anything until ``to_parquet`` is run. The reason
is that the result is not made available to users or other software.

This may sound irrelevant at first, since we are going to execute it anyway.
But being able to postpone the actual execution until a later stage, can
be extremly useful in some situations. In the example, if pandas postpones
the execution until it knows all what the user wants to do with all the data,
it could optimise the execution. For example, if the row of the spider is
going to be discarded, why load it to memory and why compute which is its
kind? In this toy example it doesn't make a difference, but imagine you
want to operate with 1Tb of data in a file, apply some transformations,
and save the result in another file in disk. With the _data analyst approach_
this is not feasible with a normal laptop, and not with pandas at the
moment even when using method chaining. But surely data engineers would
benefit from this approach.

There are related tools where this lazy execution approach is already
implemented, mainly [Dask](https://dask.org/). Dask implements a
pandas-like API, where operations are evaluated in a lazy way, and the
final task graph is not only optimized, but distributed over a cluster.
[Vaex](https://github.com/vaexio/vaex) is another example of pandas-like
API implemented with lazy evaluation.
[This talk](https://youtu.be/2Tt0i823-ec) has a demo showing how Vaex
uses lazy evaluation to deal with datasets with more than a billion
rows.

Lazy evaluation may be out of scope for pandas, but in my opinion is
another example on the different needs of the different pandas users.
From the user prespective, may be the only changes would be another
pandas option ``pandas.options.lazy_execution = True``, and possibly
a ``.collect()`` method to allow users to trigger the execution.

Another approach could be implement lazy data types. With the recently
added pandas extension arrays, custom data types can be
implemented, and having a type ``calculated_column`` could also
allow some sort of laziness. In the example, we could have a normal
DataFrame, that could have a kind column that does not actually save
the strings ``biped``, ``quadruped``,... but instead stores the
function applied, and to which column.

Whatever could be the approach, it would require major changes to
pandas internals, and it's not something that could be implemented
easily. Custom data types can be implemented, but currently some
operations will convert the data to numpy arrays, and would not
allow having a proper lazy data type.

Conclusion
----------

I think the number of pandas users, and the different kinds of work
that are being done are evidence of many good design decisions and
implementation. But conflicting interests among groups of users do
exist, and in some cases is doable to find a good solution for most
use cases. In others is not obvious and serving better our users would
require a huge amount of work.

Personally, I think a more modular pandas architecture would make it
easier to adjust to every kind of user. By having more than one version
of ``pandas.read_csv`` different users could implement solutions that
better suit their needs. Same could apply to other areas.

Another challenge is how pandas is developed. The project is mainly
developed by volunteers. Our roadmap is not determined by the needs
of your company or your industry. In my personal case, my roadmap
is determined by my personal interests on what I want to work on,
and on the kind of things I need or I want to see in pandas. If your
company would be more productive with certain pandas features or
developments, you should consider hiring someone to improve pandas
based in your interests. You can contact [NumFOCUS](https://numfocus.org/)
who manages the pandas funding, can assist with any question, and
is in direct contact with the pandas maintainers. And feel free
to [contact me](mailto:garcia.marc@gmail.com) directly too.

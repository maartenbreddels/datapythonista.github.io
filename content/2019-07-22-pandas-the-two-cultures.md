Title: pandas: The two cultures
Author: Marc
Date: 2019-07-22 23:26:00
Slug: pandas-the-two-cultures

![](/static/img/blog/two_cultures/leo_breiman.jpeg)

[Leo Breiman](https://www.stat.berkeley.edu/~breiman/) was a distinguished statistician at
UC Berkeley, known among other things for his major contributions to CART (decision trees),
and ensemble techniques, mainly bootstrap aggregation. Combining both, he was able to define
one of the most popular machine learning models even today (18 years after the publication
of the paper), [Random forests](https://www.stat.berkeley.edu/~breiman/randomforest2001.pdf).

In 2001, Breiman published the paper
[Statistical Modeling: The Two Cultures](http://www2.math.uu.se/~thulin/mm/breiman.pdf).
In it, Breiman identified that there were two somehow conflicting cultures in the discipline
of statistical modeling. One that was focusing on modeling (and trying to understand) the
stochastic process generating some random data. While the other followed an algorithmic
approach focused on obtaining results (minimizing the error between the model results and
the data), and considered the stochastic process a black box. Today we would probably call
them _statistics_ and _machine learning_, and the division between them is clear. And in a way,
machine learning is not even considered part of statistics. While this division among the two
fields may or may not be a good thing, identifying in 2001 that both communities existed, were
different and had different needs, surely helped overcome the frustration of both communities at
that time, and sped up their development. One example that illustrate the differences can be
seen on how in the area of neural networks, publishing research papers is mostly driven by 
the obtained results, more than by the theory behind the results. Ali Rahimi gave
[his view](https://www.youtube.com/watch?v=Qi1Yry33TQE) on this when receiving the test-of-time
award at NeurIPS 2017.

But this post is not about machine learning, but about [pandas](https://pandas.pydata.org/).
And about the two cultures in the pandas community, that I personally don't think are often
well identified, causing frustration to some users, and making more complex taking decisions
regarding the API of the project.

## Dr Jekyll and Mr Hyde

![](/static/img/blog/two_cultures/dr_jekyll_mr_hyde.jpeg)

To describe the two cultures, let me talk about my own professional experience.
For the last years I've been mainly working as a data scientist. Since the developers of
[scikit-learn](https://scikit-learn.org/stable/) are doing all the _fun_ work in machine learning,
and implementing all the complex algorithms for the rest of us, I'll argue that my job (and the
job of many other data scientists, some will probably disagree) is to work on data analysis to
find out what needs to be done, and data engineering to make it work in production.

What I call **data analysis** is performed in a [Jupyter notebook](https://jupyter.org/),
where I analyze and visualize the data. I found out what is wrong with it, and I quickly
grow the cells of my ``Untitled23.ipynb`` hoping I'll never have to look back at my dirty code.
What I value the most is being able to write code fast, and focus in the problem I'm solving, and
not in the code. To the extend I alias every Python library I import with incomprehensible names
like ``np``, ``pd``, ``plt``,... to make sure I save few microseconds compared to typing the actual
names. And I really appreciate the software making as many decisions as needed to save me from
having to spend the time on being explicit on what I want. Ok, this may be a bit exaggerated,
I don't really let my notebook names be untitled whatever, or use aliases, but I think you get the idea.

On the other hand, when working in **data engineering** I use vim, and I write all my code in
Python files in a clear directory structure. Every file and directory are carefully named so I can
easily find them later. Every function is well documented, and the best coding standards are applied.
All my code is version controlled with git, and code reviewed by my colleagues. I write every single
line of code knowing that I will have to revisit it many times, and I optimize for its simplicity and
its clarity.  The thing I'm more adverse to is _magic_ happening, and any software making decisions
for me. I want to be in control, I want everything in my code to be deterministic, and I want
everything in my code to be explicit. Everything that Tim Peters wrote in
[PEP-20](https://www.python.org/dev/peps/pep-0020/), the Zen of Python, applies:

- Beautiful is better than ugly.
- Explicit is better than implicit.
- Simple is better than complex.
- Readability counts.
- Errors should never pass silently.
- ...

## One pandas to rule them all

![](/static/img/blog/two_cultures/ring.jpeg)

What I find the most interesting part about _the two cultures_ I just described, is that I use
pandas for both. I think pandas is the best tool for both use cases, and I won't admit I'm biased
here, since I'm a pandas maintainer because I use the software, and not the other way round.

But how is that possible? Both use cases are radically different. Is pandas designed in a way that
is able offer both kind of users the API and features they need? Is that always possible?

The next of this post will try to find an answer by analyzing some examples.

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
could be other ways (and there are other ways that pandas supports), but creating a Series looks to
me as simple as it can be. That's what I want as a data analyst.

But as a data engineer, there are more things to consider. Imagine that my data, instead of having 3
samples, had 3 million. How much memory is pandas consuming to store in memory my data? And why?
For simplicity, let's consider only the values (and not the name of the animals):

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
pandas doesn't. Because pandas doesn't know anything about our domain, or what is reasonable,
it's deciding for us a conservative representation for our data that won't cause us problems
(as opposed as one that saves some memory).

This is working well for us as data analysts, but not as data engineers writing production code.
In this case, the Series constructor has a parameter ``dtype`` that we can use to tell pandas to not
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

In this example, pandas provides a reasonable API for both kind of users. It doesn't force us to
specify the data type when we don't care. But we're able to when we do care. Whether we want to
optimize for our system resources (mainly memory) or our own time is up to us.

### How many legs do unicorns have?

![](/static/img/blog/two_cultures/unicorn.jpeg)

An important question we face is, how many legs do unicorns have? In the previous example, we specified
they have 4, but do unicorns really have 4 legs? Did anybody have ever seen a unicorn? Let's try to be
prudent and say that we don't know how many legs they have. By convention, when we have an unknown
or missing value, we represent it as ``NaN`` (Not a Number). Every number in a computer is represented
using binary numbers (e.g. ``01001011``). ``NaN`` is represented internally as one specific sequence of
bits, reserved to have the meaning of ``NaN``. There is a convention that _translates_ how every binary
sequence corresponds to the number they represent. And this _translation_ has some exceptions, including
one value that represents the floating point number ``NaN``. If that sounds too complex, think that in
binary, ``0000`` can represent the number 0, ``0001`` the 1, ``0010``: 2, ``0011``: 3... and ``1111``: 15.
And what microprocessors manufacturers decided is something like letting represent only from 0 to 14
(instead of from 0 to 15, that we could encode with 4 bits), and reserve the ``1111`` to mean ``NaN``.
Things are in reality more complex, since ``NaN`` representations only exists for floating points numbers
(aka float), which are decimals. But that explanation should give an intuition.

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

Many things happened here. We can see, how besides the expected change of having ``NaN`` unicorn legs,
now we are back to consuming 64 bits. And not only that, but also the rest of values in the column now are
decimal (float) values. As I just explained, and can also be seen in the example on how ``NaN`` is created,
``NaN`` is a float value. Modern computers don't have an integer representation for ``NaN``, so for pandas
to do what we asked it to do, converting the column to float was the _only_ option (not really the only,
but let's pretend for a second).

It feels a bit weird to see in the Series representation that a penguin has 2.0 legs. It's conceptually
wrong, and also misleading making us believe that animals can have a decimal number of legs. There are
also technical implications too, we are consuming 4 times more memory now. And also operations among
integers don't take the same time as operations among floats at the CPU level (note that while floats
are a more complex representation, modern CPU's are highly optimized for them, and operations can even be
faster for floats than for integers).

But there is something else, see this example:

```python
>>> 0.1 + 0.2 == 0.3
False
```

Floating point numbers are approximations. They are mapping an infinite set of numbers (let's say all
real numbers) to the finite set of possible representations with 64 bits (``2 ** 64``). In many
cases using this approximate values won't make a difference (the height of a person keeps being the
same if we change the 20th decimal). But, if for example a column contains an integer id that we use
to join two data sets, converting it to floating point can mean data loss or bugs. Since floating points
are just approximations, we may try to join by ``20.0000000001 == 19.9999999999``, which won't match.
So, converting an integer column to its floating point representation can be dangerous, and probably
more for the data engineering use cases described before.

In pandas 0.24 we introduced a new data type to mix integer values with missing values. This is done
by instead of using the float ``NaN`` to represent the missing values, we internally keep a separate
Boolean array that identifies where the missing values are. This adds an extra layer of complexity
inside pandas, but avoids problems like the one just described. By default, pandas still uses the
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
when needed is very convenient for the use cases of data analysts, but in my opinion does a poor job
to the interests of precision and reliability of data engineers. And while the ``.loc[]`` syntax is very
convenient, doesn't allow us to solve the problem with a simple parameter. A new
[pandas option](https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html) could be an option
to control whether we want pandas to automatically cast columns when needed, or raise an exception instead.
But as far as I know, there has not been discussion about it.

The most popular pandas function
--------------------------------

CSV is in general a poor format to store data. It has a clear advantage, that is being able
to open CSV files in a text editor. Other than that, I think all are disadvantages:

- Inefficient storage (space that file uses in disk)
- Inefficient I/O (because the volume of data, and also the required casting)
- Lack of types (everything is a string in a CSV, so original types are lost)
- Lack of a standard (different quoting, delimiters,...)

Despite of those, CSV happens to be one of the most popular formats out there, being the
page [pandas.read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)
the one with most visits in the pandas documentation.

To manage all the trickiness of the format, ``pandas.read_csv`` provides as much as 50
arguments, to customize for your file format, and for your needs.
[StaticFrame](https://github.com/InvestmentSystems/static-frame) a project (somehow)
aiming to compete with pandas, contains the next sentence in its README file:

> The Pandas CSV reader far out-performs the NumPy-based reader in StaticFrame: thus, for now, using Frame.from_pandas(pd.read_csv(fp)) is recommended for loading CSV files.

This gives an idea of all the complexity in the CSV parser, not only in terms of the parameters,
but also in terms of how optimized it is for performance.

Despite being one of the most powerful and optimized CSV parsers out there,
[James Powell](http://twitter.com/dontusethiscode) gave a
[lightning talk at PyData London 2019](https://www.youtube.com/watch?v=QkQ5HHEu1b4&t=1554)
on how the parser could be easily improved in several ways for a use case he's got.

Those include:

- Assume string columns are properly encoded and load them directly into memory
- Optimize date casting by assuming a specific format, and a limited set of values

Again, no matter the great job done in implementing pandas, the software is
being unable to fully satisfy all user cases. ``pandas.read_csv`` does again a
good job at making life easy to data analysts (as defined at the beginning of this
post). And it also does an impressive job at adding parameters to empower users that
know what they are doing and have production-ready code need (data engineers). But
even with an insane number of parameters like 50, looks like loading a CSV file into
memory may be too complex for a single generic function.

What is the solution here? Personally, I think that having _one pandas to rule them all_
is still possible and the best option. But not a ``pandas.read_csv`` to rule them all.
My view is that pandas shouldn't include I/O modules that are able to load data from
every possible format, and in every possible way. That's just impossible.
But pandas could do a better job at allowing and encouraging an ecosystem of I/O
pandas plugins. I proposed in [this issue](https://github.com/pandas-dev/pandas/issues/26804)
a first refactoring that would make this possible. It is still under discussion,
since the proposed changes are big.  I'll write in a different article more details about this proposal.

Lazy pandas
-----------

![](/static/img/blog/two_cultures/lazy_pandas.jpeg)

To conclude this article, I will talk about what in my opinion is one of the biggest
differences between the needs of data analysts using pandas in a Jupyter notebook,
compared to data engineers using it to write production pipelines.

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
to visualize how our data looks like. We also may need not only to visualize the
data, but _understand_ or verify it, for example by checking which is the median
of one column. It is likely that at the end of writing that code, we don't care
about it anymore, since we already verified what was in the data, and extracted
the insights we care about.

In the second case, while doing almost the same, the code is written to be read
and to be maintained. If there is a bug in the code, it should be easy to
understand what it does, and fix it. The goal is not to discover anything
while writing the code. But just to add a functionality to a system, and to be
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
is that the result is not made available to the user or anywhere else.

This may sound irrelevant at first, since we are going to execute it anyway.
But being able to postpone the actual execution until a later stage, can
be extremely useful in some situations. In the example, if pandas postpones
the execution until it knows all what the user wants to do with all the data,
it could optimize the execution. For example, if the row of the spider is
going to be discarded, why load it to memory and why compute which is its
kind? Some memory and some computation power and time can be saved. In this
toy example it doesn't make a difference, but imagine you want to operate
with 1Tb of data in a file, apply some transformations,
and save the result in another file in disk. With the _data analyst approach_
this is not feasible when running the code in a normal laptop. And while
pandas is not able to work in an out-of-core way, or optimize the execution
even when using method chaining, that could be implemented.

There are related tools where this lazy execution approach already
exists, mainly [Dask](https://dask.org/). Dask implements a
pandas-like API, where operations are evaluated in a lazy way, and the
final task graph is not only optimized, but distributed over a cluster.
[Vaex](https://github.com/vaexio/vaex) is another example of pandas-like
API implemented with lazy evaluation.
[This talk](https://youtu.be/2Tt0i823-ec) has a demo showing how Vaex
uses lazy evaluation to deal with data sets with more than one billion
rows.

Lazy evaluation may be out of scope for pandas, and there are many things
that should be changed even before being considered. But in my opinion is
another example on the different needs of the different pandas users.

I guess a dual pandas would be possible, and for the user, may be a
simple pandas option ``pandas.options.lazy_execution = True`` would be enough.
Together with few methods to allow users to trigger the execution of a task
graph (e.g. a ``.collect()``).

There are also other approaches that could be considered. With the recent
addition of [pandas extension arrays](https://pandas.pydata.org/pandas-docs/stable/development/extending.html#extension-types),
custom data types can be implemented. And having types for memory
maps, or calculated columns could be an option that could allow
some sort of laziness. In the example, we could have a normal
DataFrame, that could have a kind column that does not actually save
the strings ``biped``, ``quadruped``,... but instead stores the
function applied, and to which column. The actual lookup could then
happen after the data is filtered.

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
exist. In some cases is doable to find a good solution for most
use cases. In others is not obvious and serving better our users would
require a huge amount of work.

Personally, I think a more modular pandas architecture would make it
easier to adjust to every kind of user. By having more than one version
of ``pandas.read_csv`` different users could implement solutions that
better suit their needs. Same could apply to other areas.

But probably the most important challenge to get those implemented is
not what is the technical solution, but it's in how pandas is developed.
The project is mostly developed by volunteers, including the maintainers
(the people who review the contributions, discuss in the issues that
users open...). Our roadmap is not determined by the needs
of your company or your industry. In my personal case, my roadmap
is determined by my personal interests on what I want to work on,
and on the kind of things I need or I want to see in pandas myself.
If your company would be more productive with certain pandas features or
developments, you should consider hiring someone to improve pandas
based in your interests. You can contact [NumFOCUS](https://numfocus.org/)
who manages the pandas funding, can assist with any question, and
is in direct contact with the pandas maintainers. Besides hiring someone
in your own team, you could also provide funds to develop pandas that
are managed by NumFOCUS. Also feel free to [contact me](mailto:garcia.marc@gmail.com)
directly if you want more advice, and are interested in this.

The pandas ecosystem
====================

I think it is easy to agree that pandas is a huge project. The idea behind
pandas is to provide users a single package to extract, manipulate and
analyze data. While I belive this design is one of the main reasons for
the project succes, there would also be advantages on a more
modular design. Thinking of pandas more as a framework than as a
*batteries included* package.

In this post I will describe the current and potential modular design of
pandas, and other packages that help pandas accomplish its mission.

Let me start by dividing the project in different components. There are
other possible divisions of the project, but the next one will help discuss
how pandas interact with the rest of the world.

First, pandas contains a **backend**. If we imagine a minimal version of pandas,
the basic component of the project are probably the `Series` and `DataFrame`
data structures. May be they would not contain much more functionality than
previwing the data, and returning some metadata like the shape and types, but
it is difficult to imagine even a minimal version of pandas without them.

Second, one of the key features of pandas is its **indexing** system. Being
able to access data by a position in one of the axis by a descriptive name.

Then, we need an **I/O** module, so `Series` and `DataFrame` can be loaded
and exported to other systems, from databases to plain text formats like csv,
to binary formats parquet.

Once we have the data structures and the ability to load data to them, next
by priority could possible by all the functionalities to **transform** data.
In this space, pandas provides features for joining, concatenating, reshaping,
grouping, creating windows, string manipulation and others.

With these components, pandas can be used as a powerful ETL software. ETL
stands for Extract, Transform and Load data. So, we could build pipelines
that extract data from different sources, join them, aggregate the data,
clean imperfections and export it to a file in disk.

The next thing we would possibly like to add to pandas is its **analysis**
functionality. For example, statistical functions like the *mean*, *mode*,
*standard deviation*,... will fall in this component.

Finally, and related to using pandas as a data analysis tool, we also
have the **plotting** functionality.

Summarizing, we can divide pandas in the next components:

- Backend and data structures
- Indexing
- Input / Output
- Data transformation
- Data analysis
- Plotting

The division may not be perfect, but it should be useful to discuss
on how different components of pandas interact with the rest of the
world. We will now analyse them one by one.

Backend and data structures
---------------------------

Python and numpy
~~~~~~~~~~~~~~~~

The current pandas implementation is based on `numpy`. While Python is
an extraordinary language that is serving extremly well the open source
community, it was never design with large volumes of data in mind.

Without going into the details, Python is design for simplicity and
flexibility, allowing code like:

```python
my_list = [0, 3.1415, 'foo']
```

Which required that every object in the list stores its type with it.
So the first value will not only store the value ``0``, but also that
the bits internally representing the value of zero (e.g. ``000000``)
should be considered an integer, and not another type.

But when we have something like:

```python
my_list = [1, 2, 3, 4, 5]
```

We are not making use of this flexibility, but Python will still
store the type (and more information) for every value in the list.
For a list of 5 elements that is not significant, but as our data
becomes bigger, the penalty we pay in memory requirements and speed
increases.

`numpy` is the de-facto standard in Python for a more performant
(and less flexible approach). Of course it is more than that, but
to keep it simple, `pandas` uses `numpy` to store the data in
`Series` and `DataFrame` objects, and that makes `pandas` require
less memory and perform much faster compared to a version backed
by Python lists.

pandas backend alternatives
~~~~~~~~~~~~~~~~~~~~~~~~~~~

But `numpy` was not designed as a backend for `pandas`, but more
as a package to operate over matrices. And while `numpy` has made `pandas` the
great tool is it, it also imposes some limitations. Including an extra layer
of complexity in `pandas` internals (mainly the `BlockManager`).

Ideally, the `pandas` backend should be able encapsulate all the internal
representation of `Series` and `DataFrame`, and expose a low level API
for the rest of `pandas` components to interact with. This would allow
for several projects to "compete" and try different approaches, without
having to reimplement the whole of `pandas`.

The most obvious alternative to the current backend is one based in
`Apache Arrow <https://arrow.apache.org/>`_. Arrow is a project led by
`Wes McKinney <https://wesmckinney.com/>`_, the creator of `pandas`, and the
aim of `Arrow` is not only become a backend for `pandas`, but a backend
for any project based on tabular data (e.g. `R`). This will not only create
synergies, but will also allow for much better interoperability among the
different tools.

Another possible implementation of the `pandas` backend could be based on
`PyPy <https://www.pypy.org/>`_. The main advantage of a `PyPy` backend would
be its simplicity. The backend could be implemented in regular Python, and
the `PyPy` Just-in-time compiler would take care of making the code faster and
memory efficient. This would make the implementation extremly easy compared
to the other approaches, which require C, C++ or Fortran implementations.
While `PyPy` is not currently designed to optimize large lists or to manage
types, based on the discussions I had with its maintainers, it is something
feasible to have.

The current state
~~~~~~~~~~~~~~~~~

The scenario just described is more ideal than the current state. Right now
`pandas` is very coupled to `numpy`, and there is not a clear backend. Even
designing what should be in the backend, and what in the application layer
is far from trivial. There is a consensus on moving towards an `Arrow`
backend in a non-immediate future, but the how and the when is not yet
defined.

Over the last past year, a lot of work in the project has been focused on
extending the current backend with new types. What is known as
`pandas extension arrays <https://pandas-dev.github.io/pandas-blog/pandas-extension-arrays.html>`_.
This has been a huge amount of work, but much simpler than isolating and
replacing the current backend. The idea is to keep using `numpy` for
`numpy` supported types (e.g. `int`, `float`,...) and have an API to
be able to extend `pandas` with custom types.

Opening `pandas` types to be extended made the design of already custom
pandas types much simpler (e.g. `datetime with timezone`, `Period`,...),
and allowed the creation of third-party projects that enrich `pandas`,
for example `cyberpandas <https://github.com/ContinuumIO/cyberpandas>`_
for ip addresses and masks, and
`Fletcher <https://github.com/xhochy/fletcher>`_ for more efficient strings.

Indexing
--------


Input / Output
--------------


Data transformation
-------------------


Data analysis
-------------


Plotting
--------


Summary
-------

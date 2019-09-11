Title: Dataframe summit @ EuroSciPy write up
Slug: dataframe-summit-at-euroscipy
Tags: pandas

Last week took place in Bilbao, Spain, [EuroSciPy 2019](https://www.euroscipy.org/2019/).
This year we introduced the [maintainers track](https://www.euroscipy.org/2019/maintainers.html)
a room dedicated to discussions among maintainers. The idea is similar to the 
[birds of a feather](https://en.wikipedia.org/wiki/Birds_of_a_feather_(computing)) or unconference
sessions of other conferences. But focussed on open source maintainers and contributors. And
we scheduled most of the sessions in advanced, to attract the interested people to join the
conference. We also had a maintainers plenary session, in which 26 maintainers of popular
open source scientific projects participated (my guess is that around 50 maintainers attended
the conference).

## Dataframe summit session

One of the sessions was a 2 hours discussion on Python dataframes. 16 people attended it, around
half of them were maintainers of dataframe open source libraries. There were also pandas users
and contributors, maintainers of other projects (PyPy, pytest) and people interested in being involved.
Also the developer of a proprietary dataframe library in Python, who could also add value to the discussion.

![](/static/img/blog/dataframe_summit.jpeg)

Those were the libraries represented:

- **[pandas](https://github.com/pandas-dev/pandas)** Flexible and powerful data analysis / manipulation library for Python
- **[Dask](https://github.com/dask/dask)** Parallel computing with task scheduling
- **[Vaex](https://github.com/vaexio/vaex)** Out-of-Core DataFrames for Python
- **[Modin](https://github.com/modin-project/modin)** Scaling pandas with [Ray](https://github.com/ray-project/ray/)
- **[xframe](https://github.com/QuantStack/xframe)** DataFrame library in C++

We started by personal introductions, project introductions, and what people wanted to get out
of the session (many people already proposed topics before the event, and we defined an agenda with those).

### Document the ecosystem

One of the first topics discussed was on how to let users know what is the best dataframe
tool for their job, and how the existing packages are different. The general consensus was
that the [pandas ecosystem](https://pandas.pydata.org/pandas-docs/stable/ecosystem.html) page
is the best place for it. There are already plans to improve this page (and plans and work in progress to improve
the look and feel of the pandas website and documentation).

### Apache Arrow

Another topic that was discussed early was **[Apache Arrow](https://arrow.apache.org/)**. Arrow's mission is to
provide a common memory representation for all dataframe libraries. So, libraries don't need to reinvent the
wheel, and transferring data among packages (e.g. pandas to R) can be done without transformations or even without
copying the memory.

Vaex is already using Arrow, and pandas has plans in its [roadmap](https://pandas.pydata.org/pandas-docs/stable/development/roadmap.html)
to move in that direction. People were in general happy with the idea, but there were some concerns
about decisions made in Arrow (mainly contributed by Sylvain, from xframe):

- Apache arrow C++ API and implementation not following common C++ idioms
- Using a monorepo (including all bindings in the same repo as Arrow)
- Not a clear distinction between the specification and implementation (as in for instance project Jupyter)

### Interoperability

The next topic was about **interoperability**. How dataframe libraries can interact among them, and
with the rest of the ecosystem. Examples can be:

- Using the same plotting backends from different dataframe libraries
- Passing to [scikit-learn](https://scikit-learn.org/stable/index.html) pandas-like dataframe objects

There was consensus that defining a standard (and minimal) dataframe API would help. Dataframe libraries
could extend this smaller API and offer users a much bigger APIs (like pandas). But having a subset of
operations and methods would be very useful for third party libraries expecting dataframe objects.

Devin from Modin is doing research at UC Berkeley on defining this API, and he's already got some
documentation he's happy to share. Modin is already implemented with this design, and while it's
one of the less mature participating projects (in Devin's words), it's user-facing layer could
potentially be reused by other projects reimplementing dataframes with a different backend.

It was noted that could be useful to have a common test suite, if a standard dataframe API is defined.
There was agreement that the pandas test suite is not appropriate for other packages.

### Public API improvements

At the end of the session, we discussed about possible improvements to the public pandas API.
Since several of the participants reimplemented the pandas API, was a good opportunity to see
places where they found inconsistencies, or where the API was making their lives difficult
when using other approaches.

Indexing was the part of pandas that other maintainers were less happy about. The way `.loc`
behaves was one of the comments. And being forced to have a default index, and not being able
to index by other columns were other comments.

### Next steps

Couple of things were discussed to keep those discussions active, and keep coordinating on
shaping the dataframes of the future.

The first was to start a workgroup, or a distribution list (or discourse). The `pandas-dev`
list wasn't used by the participants (except the pandas maintainers), and it didn't seem
to be the appropriate place.

Another idea would be to organize another bigger dataframe summit in the future. It was
proposed to be hosted somewhere in the Caribbean (ok, it was me who proposed that, and
everybody else laughed, but here I leave it again). :)

An update on the pandas documentation
#####################################

Some context
------------

This post is mainly a technical post on what's the status of the pandas documentation.
But let me provide a bit of context on where this comes from.

It's a personal opinion, but I think pandas is one of the clearest examples of a new
revolution in the free software world. Probably responsible of the huge growth of
Python, a language that that not many people knew about when pandas started around 10
years ago, even if now it's hard to believe.

And I think its documentation has been the clearest example of the paradox of open
source. While pandas users were growing to the millions, and it was adopted in thousands
of companies (including the largest companies in the world), almost nobody spent any time
or money in its documentation (which requires a lot of work to keep updated and consistent).
It's surely not to blame the around 3 people who took the responsibility of maintaining pandas,
and were busy not only making pandas survive and handle the huge increase in its user base,
but making the tool as great as it is and improving it in every version. That work was done mainly
in weekends, commutes and evening after work, by volunteers who had an unrelated full time job.

Around 2 years ago I sent to the project my first pull request, fixing a single docstring
(one of the 1,300 in the project). Since then, I spent significant amounts of time working
on the pandas documentation, and encouraging and mentoring people to work on it too.
Many people told me that they saw significant improvements in the pandas documentation in
the last couple of years. But there is still a lot of work to do.

This post is a summary of what has been done, and the roadmap on what's pending until pandas
has one of the best documentations of any open source project, the one that it deserves.
This roadmap was discussed with several participants of the
[European pandas summit](https://python-sprints.github.io/europandas2019/), that happened at
the beginning of this year. But while I expect few changes to it, discussion about the
points mentioned here is highly encouraged (and not only restricted to pandas maintainers,
but from anyone interested in helping make the documentation of pandas better).

**If you work for a company that is making money using pandas, and that would be more productive
and make even more money if pandas documentation was better, please contact a pandas maintainer
including [myself](mailto:garcia.marc@gmail.com) or [NumFOCUS](https://www.numfocus.org).
We are happy to discuss funding opportunities, including small grants and helping your company
hire people to work on pandas.**

The problem with the docstrings
-------------------------------

The pandas API is huge, and includes around 1,500 pages (functions, methods, classes...).
Given the very limited amount of people who developed the library, many of these API pages couldn't be
created when the features were implemented, with the standards a library like pandas
should have. See for example the
`Resampler.last <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.core.resample.Resampler.last.html>`_
page.

It may not be obvious for people who haven't contributed to a project like pandas before,
but improving a docstring, and make it as useful for users as possible, it's not 5 minutes
of work. Based on the work done by lots of contributors over the last year, I would estimate
it takes around 1 day of work of an experienced pandas user. You can see the docstring of
`Resampler.bfill <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.core.resample.Resampler.bfill.html>`_
to see what I'd consider a good docstring.

Considering this estimate of 1 day per docstring, and the around 1,300 docstrings, it's
easy to calculate that it'd take around 5 years for a single person working full time,
to have all them fixed.

The pandas documentation sprint
-------------------------------

As it's obvious that a single person can't do much, one of the things that was tried
was to organize a `huge sprint <https://python-sprints.github.io/pandas/>` to work on
docstrings. While the sprint was probably successful in some ways, with 30 local user
groups in different parts of the world (Korea, India, Kenya, Nigeria, Argentina, and
many other locations, mainly in US and Europe). Around 500 participants worked in
fixing docstrings, and around 200 docstrings improved significantly. That
was in a way extremly great (and 200 out of 1,500 leaves a lot of work but it's a
significant contribution). But not everything was so positive in may opinion, and surely
not an option to repeat the experience in the same way. That is because the bottleneck
was not in attracting new contributors (the response of the community was amazing),
but the core development team, and the reviewers. The sprint distracted the team from
any other development for more than two weeks, and increased massively the amount of work
of a small team of volunteers that already do more than they can. I took care personally
of the last pull requests of the sprint, and that was more than 6 months after it happened.

It's worth repeating how amazing was the response of the community on participating
in the sprint and helping develop pandas. And besides all the enthusiastic people who
joined, I think it's fair to give a big part of the credit to `NumFOCUS <https://numfocus.org/`
for creating a strong PyData community, and opening the channels to reach the more than 500 pandas
users who wouldn't mind spending a whole Sunday working on the pandas documentation. That's really
impressive I think, and now that the community is so healthy, it may be easy to forget the
amount of work it takes to build a community with around 150 local user groups, and between 10
and 20 conferences per year.

But that alone doesn't fix the problem, since as mentioned, the bottleneck wasn't on the
number of contributors, but in the number of maintainers.

The validation script
---------------------

We anticipated before the sprint, that reviewing the contributions would be a lot
of work. And we developed a script to automate part of it. The idea was to automatically
detect things like:
- The documented parameters of a function don't match the actual parameters in the signature
- Conventions like starting sentences with a capital letter or finishing with a period are not satisfied
- Some sections we'd like to always have (like Examples) is not present.
- Formats that make sphinx render the documentation incorrectly, like missing spaces before colons...

We managed to have several of these ready for the sprint. But to keep all the docstrings consistent
and rendering correctly, we needed many more. Many people spent a significant amount of time adding
new checks to the script, and we are currently able to automatically detect
`more than 40 possible problems in docstrings <https://github.com/pandas-dev/pandas/blob/master/scripts/validate_docstrings.py#L63>`_.

Of course not everything can be validated, think of correct grammar, wrong, inaccurate or misleading
information, examples that are not clear... But validating almost every formatting issue automatically
will definitely save a lot of time of reviewers. Who will be able to focus on the things that
can't be automated.

Continuous Integration
----------------------

During the sprint, we provided clear instructions, and we had mentors in each of the 30 different
locations. So, everybody was probably aware that the validation script was one of the main things
they had to check. But regular contributors don't get this sort of induction. So, ideally we would
like to run the checks automatically in the CI, that's what it is for. But there are some things
to consider.

With Travis, our main CI system, the errors ended up in a huge log, that only experienced
pandas developers are able to understand. See for example `this job <https://travis-ci.org/pandas-dev/pandas/jobs/484898115>`_
and make sure you wait until it's fully loaded. :)

Luckily, at the time this was implemented, numba set up Azure Pipelines for their CI, and we
decided to use it to complement Travis. The main reason was that we required more computational
power for the huge test set of pandas, and the large number of builds. But, I think the clarity
on how the errors can be reported, is as convinient as the 30 concurrent jobs the Azure team
offered us. Compare this with the previous Travis log:

.. image:: https://user-images.githubusercontent.com/10058240/47961709-1ca90800-e008-11e8-80d7-cccc2c2e5776.png

We were very ambitious, and somehow pioneers in what we were doing, and it wasn't
easy to get what we wanted. But The Azure team was extremly helpful, and the final
presentation of errors in docstrings, as well as the linting errors and others was
much clearer. And friendly for first time contributors.

We never worked on it, but I think an obvious next step would be to extract this list
of errors, and publish a comment back to GitHub with them. Besides making it even clearer
and more compact, an important advantage is that the contributor would receive an email
from GitHub with these errors. And for first time contributors who won't probably check
the CI status, that can make the process even more efficient. I see things moving much
faster if the contributor receives the message 30 minutes after opening the PR, while they
are likely to still be available. Than wait couple of days until a reviewer has to manually
send the message, and the contributor is potentially back to their work, and not having
time to work until several days later.

But this part of publishing the result of the CI is not trivial, and is left as an
exercise to the reader. Or to the Azure team, this is something that I think would be
very useful to most projects.

Validating docstrings in the CI
-------------------------------

Two key pieces to validate contributions to the pandas docstrings are in place:
- A validation script with lots of checks
- A CI system friendly with first time contributors

But there is a last piece needed. If we activate the validation in the CI, we will
have 1,000 docstrings or more reporting errors in the CI for every PR (whether it's
related to documentation, or anything else).

Ideally, we could identify the docstrings that have been modified, and just validate
those. But with a language like Python, that let's you do all sort of magic with code,
and even create code dynamically, that's a problem almost as complex as pandas itself. ;)

This leaves us in a unfortunate position, of only being able to validate what has
already been fixed. Which is extremly useful, as we can guarantee that things don't
get worse. But it doesn't solve our problem of improving the docstrings that need it.

So, what was the plan here? I would divide the docstring checks in two categories:
- The pure formatting things (like having periods at the end of sentences)
- The ones that require knowledge of pandas and object being documented (like adding examples or an undocumented parameter)

The ones in the first category are somehow easy to fix, and 100 docstrings can be
fixed for one of the docstring in a single PR in a reasonable amount of time. By doing
this, single errors can be added to the docstring, and we can "forget" about them.

For example, if all the docstrings that have a description, have every paragraph ending
with a period, we can add this to the CI. And all the docstrings that don't have a description
or that new paragraphs need to be added, we will automatically validate that are created with
the period.

We already completely fixed 7 of the more than 40, and we validate that the errors are
not added again:
- GL06: An unknown section is found
- GL07: Sections in the wrong order
- GL09: Deprecation warning in the wrong position
- SS04: Summary contains heading whitespaces
- PR03: Parameters are in the wrong order (compared to the signature)
- PR05: Parameter type finishing with a period (it shouldn't)
- EX04: pandas or numpy explicitly imported in the examples (we assume they are always imported)

But there are still many errors that need to be fixed. With the same validation script,
when no specific docstring is provided, we can validate all them, and output the result
to a json file::

   $ ./scripts/validate_docstrings.py --format=json > docstrings.json

That can easily be loaded into pandas, and see what needs to be fixed and what not.

.. code-block:: python

   (pandas.read_json('docstrings.json', orient='index')
          .loc[:, 'errors']
          .map(lambda err_list: '|'.join([err[0] for err in err_list]))
          .str.get_dummies('|')
          .sum(axis='index')
          .sort_values()
          .plot.barh())

We can see how there are more than 500 objects that they don't have any documentation.
See `Series.empty <http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.empty.html>`_
for an example on how this is shown in the documentation.

Almost as much that have issues with the formatting of what is being returned. And in
some cases, there are just few cases left for some of the errors.

As I mentioned before, some of these errors could be fixed in all the docstrings at once,
while in some other cases, it makes more sense to fix the whole docstring at once.

Doing all the "quick" formatting fixes first has the advantage, that once the work on a
full docstring is performed, the CI will be able to warn of any formatting issue.

Where do we come from?
----------------------

If you are wondering what was the status of the pandas documentation (the docstrings)
before the sprint, the validation docstring, and all the work many people did in the
last 

# An update on the pandas documentation

## Some context

This post is mainly a technical post on what's the status of the pandas documentation.
But let me provide a bit of context on where this comes from.

It's a personal opinion, but I think pandas is one of the clearest examples of a new
revolution in the open source world. A project that contributed to the huge growth of
Python, a language that not many people knew about when pandas development started.

And I think its documentation has been the clearest example of the paradox of open
source software. While pandas users were growing to the millions, and it was adopted in thousands
of companies (including the largest companies in the world), almost nobody spent any time
or money in its documentation (requiring a lot of work). It's surely not to blame the
very few people (3 or 4 at times) who were maintaining the project, dealing with thousands of
issues, updates in the many and fast changing dependencies, releasing new versions... While also
implementing new features and fixing bugs themselves. And even more considering that most of that
work was done as volunteers, in evenings after work or in weekends.

Around 2 years ago I sent to the project my first pull request, fixing a single docstring
(one of the more than 1,500 in the project). And decided to spend a significant amount of
my also volunteer time (after work and during weekends) in improving that part. That also
was one of the main reasons for starting the [Python sprints](https://python-sprints.github.io)
group.

More than two years later, not much changed (apparently). But if you care about my opinion,
I'm sure very soon pandas will have one of the best documentations of any open source project. This
post explains all the work done by hundreds of people in the last couple of years, and the work
that is still missing, and how we are going to approach it.

**If you work for a company that is making money using pandas, and that would be more productive
and make even more money if pandas documentation was better, please contact a pandas maintainer
including [myself](mailto:garcia.marc@gmail.com) or [NumFOCUS](https://www.numfocus.org).
We are happy to discuss funding opportunities, including small grants and helping your company
hire people to work on pandas.**

## The problem with the docstrings

The pandas API is huge, and includes around 1,500 functions, methods, classes, attributes...
Each of them with a pange in the documentation.
Given the very reduced number of developers pandas had, and the huge demands of a dataframe
library in Python, most of those API pages couldn't be
created with high standards when the features were implemented. See for example the
[Resampler.last](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.core.resample.Resampler.last.html)
page.

It may not be obvious for people who haven't contributed to a project like pandas before,
but improving a docstring, and make it as useful for readers as possible, it's not 5 minutes
of work. Based on the work done by lots of contributors over the last year, I would estimate
it takes around 1 day of work of an experienced pandas user. You can see the docstring of
[Resampler.bfill](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.core.resample.Resampler.bfill.html)
to see what I'd consider a good docstring.

Considering this estimate of 1 day per docstring, and the around 1,500 docstrings, it's
easy to calculate that it'd take more than 5 years for a single person working full time,
to have all them fixed. And that excludes the time of maintainers to review the changes,
provide feedback, merge...

## The pandas documentation sprint

As it's obvious that a single person can't do much, one of the things that was tried
was to organize a [worldwide pandas sprint](https://python-sprints.github.io/pandas/).

The sprint was extremely succesful in many ways. 30 local users groups participated,
from places as diverse as Korea, Hong Kong, India, Turkey, Kenya, Nigeria, Argentina
or Brazil, besides many cities in Europe and US. Difficult to say how many people
participated, but we estimate there where around 500 people helping make pandas
documentation for a whole Saturday.

I think there are no words to describe how amazing that is. How many people offered
to organize sprints with their local groups. The organizers had to prepare the event
for weeks, both for logistics but also for the technical part of leading a lot of
people in their first open source contributing. And also amazing the amount of people
who joined each of those local events.

A big responsible for this success was [NumFOCUS](https://numfocus.org/). For several
years now NumFOCUS has done extraordinary efforts on building the PyData community.
Having a connected network of more than 100 user groups made it very easy to commuinicate
and reach all the people who could be interested.

The feedback I received from the participants and organizers was very positive, and people
enjoyed the experience (which I personally think it's much more important than the
contributions made). And there were around 200 documentation pages that were fixed
because of the sprint (13% of the total).

But not everything was so positive. The sprint also made evident that the problem of
fixing the documentation was not the number of contributors. The bottleneck happened
to be the maintainers. The sprint created a total disruption of the project for two
weeks. And this wasn't much longer because the maintainers were spending day and night
reviewing the pull requests from the sprint. In many cases it was the maintainers who
had to finish the work started during the sprint. Many pull requests contained great
work, but were discontinued, and they required important changes that had to be done
by the maintainers. The last PR from the sprint was merged almost a year later than
the sprint.

## The validation script

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
[more than 40 possible problems in docstrings](https://github.com/pandas-dev/pandas/blob/master/scripts/validate_docstrings.py#L63).

Of course not everything can be validated, think of correct grammar, wrong, inaccurate or misleading
information, examples that are not clear... But validating almost every formatting issue automatically
will definitely save a lot of time of reviewers. Who will be able to focus on the things that
can't be automated.

## Continuous Integration

During the sprint, we provided clear instructions, and we had mentors in each of the 30 different
locations. So, everybody was probably aware that the validation script was one of the main things
they had to check. But regular contributors don't get this sort of induction. So, ideally we would
like to run the checks automatically in the CI, that's what it is for. But there are some things
to consider.

With Travis, our main CI system, the errors ended up in a huge log, that only experienced
pandas developers are able to understand. See for example [this job](https://travis-ci.org/pandas-dev/pandas/jobs/484898115)
and make sure you wait until it's fully loaded. :)

Luckily, at the time this was implemented, numba set up Azure Pipelines for their CI, and we
decided to use it to complement Travis. The main reason was that we required more computational
power for the huge test set of pandas, and the large number of builds. But, I think the clarity
on how the errors can be reported, is as convinient as the 30 concurrent jobs the Azure team
offered us. Compare this with the previous Travis log:

![](https://user-images.githubusercontent.com/10058240/47961709-1ca90800-e008-11e8-80d7-cccc2c2e5776.png)

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

- **GL06**: An unknown section is found
- **GL07**: Sections in the wrong order
- **GL09**: Deprecation warning in the wrong position
- **SS04**: Summary contains heading whitespaces
- **PR03**: Parameters are in the wrong order (compared to the signature)
- **PR05**: Parameter type finishing with a period (it shouldn't)
- **EX04**: pandas or numpy explicitly imported in the examples (we assume they are always imported)

But there are still many errors that need to be fixed. With the same validation script,
when no specific docstring is provided, we can validate all them, and output the result
to a json file::

    $ ./scripts/validate_docstrings.py --format=json > docstrings.json

That can easily be loaded into pandas, and see what needs to be fixed and what not.

```python
(pandas.read_json('docstrings.json', orient='index')
      .loc[:, 'errors']
      .map(lambda err_list: '|'.join([err[0] for err in err_list]))
      .str.get_dummies('|')
      .sum(axis='index')
      .sort_values()
      .plot.barh())
```

We can see how there are more than 500 objects that they don't have any documentation.
See [Series.empty](http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.empty.html)
for an example on how this is shown in the documentation.

Almost as much that have issues with the formatting of what is being returned. And in
some cases, there are just few cases left for some of the errors.

As I mentioned before, some of these errors could be fixed in all the docstrings at once,
while in some other cases, it makes more sense to fix the whole docstring at once.

Doing all the "quick" formatting fixes first has the advantage, that once the work on a
full docstring is performed, the CI will be able to warn of any formatting issue.

## Where do we come from?

If you are wondering what was the status of the pandas documentation (the docstrings)
before the sprint, the validation docstring, and all the work many people did in the
last 


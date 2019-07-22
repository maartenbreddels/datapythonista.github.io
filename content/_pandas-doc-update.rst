An update on the pandas documentation
#####################################

Some context
------------

This post is mainly a technical post on what's the status of the pandas documentation.
But let me provide a bit of context on where this comes from.

It's a personal opinion, but I think pandas is one of the clearest examples of a new
revolution in the free software world. Probably responsible of the huge growth of
Python, a language that very few people knew about when pandas started.

And I think its documentation has been the clearest example of the paradox of open
source. While pandas users were growing to the millions, and it was adopted in thousands
of companies (including the largest companies in the world), almost nobody spent any time
or money to its documentation (requiring a lot of work). It's surely not to blame the
around 3 people who took the responsibility, and were busy making the tool as great as it
is, mainly in their weekends and evening after work.

Around 2 years ago I sent to the project my first pull request, fixing a single docstring
(one of the 1,300 in the project). This week I worked with other pandas developers in a
new clearer structure, and making the documentaion homepage more useful to find all the
existing pages.

I'll leave the personal details for another blog post I'll probably never write. But
this post is intended as a hand over, for anyone interested in continuing the work
on the documentation. While I may or may not continue working on pandas or other free
software projects, I don't plan to spend more time on the documentation.

The problem with the docstrings
-------------------------------

The pandas API is huge, and includes around 1,300 pages (functions, methods, classes...).
Given the very limited resources of the library, many of these API pages couldn't be
created when the features were implemented with the standards a library like pandas
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
was to organize a `huge sprint <https://python-sprints.github.io/pandas/>`. While the 
sprint was probably successful in some ways, with 500 participants we managed to get
around 200 docstrings improved significantly. But that was at the cost of keeping
the whole core development team distracted from any other development for two weeks
or more. A fun experience for the many who participated I'd say, but something that
I wouldn't like to see repeated (at least in the same way).

The good news was that with all the efforts of `NumFOCUS <https://numfocus.org/` to
create a strong PyData community, it was somehow easy to find 500 pandas users who
wouldn't mind spending a Sunday working on the pandas documentation. That's really
amazing I think.

But the bad news is that the bottleneck is not there. But in the reviwing of the
work. It's expected that people making their first contribution require mentorship
and feedback from more experienced developers.

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

Today I've got my new Dell XPS (with Ubuntu preinstalled), and this is the procedure
to set it up, and get my perfect working environment. This is expected to be useful
mainly for my **future self**, but sharing it here in case someone else can find
ideas or tips that are useful. Also happy to receive comments on how you do things
differently (and potentially better).

My operating system of choice is `Fedora MATE Compiz <https://spins.fedoraproject.org/mate-compiz/>`_,
I think GNOME 3 was a big mistake, so staying in what was GNOME 2.

After downloading the ISO, I create the live USB with `UNetbootin <https://unetbootin.github.io/>`_.
This works well, but it has a problem. The label of the volume is not updated, and it becomes inconsistent
with the one that GRUB loads. This will create a lot of warnings like this::

   dracut-initqueue[602]: Warning dracut-initqueue timeout - starting timeout scripts

With couple of final warnings::

   Warning: /dev/disk/by-label/Fedora-Live-WS-x86_64-29-1 does not exist
   Warning: /dev/mapper/live-rw does not exist

To fix it, we just need to know the label of our live USB (can be obtained in the rescue terminal by
calling ``blkid``). And then, in the GRUB menu, press `e` with the `Start Fedora Live` option
selected, and replace the value of `LABEL` by the correct one. A `Ctrl-x` will make the system
boot with the updated configuration, and should start normally. This
`video <https://www.youtube.com/watch?v=C3iSqmfPRxY>`_ shows the process step by step.

The default configurations during the installation work well for me (using 50Gb for `/`, the rest
for `/home/`, and `ext4` filesystem). But I encrypt `/home/`, which is not enabled by default.

Once the new system is installed, and running, those are the tasks I perform.

Configuration
-------------

- Merge both panels into one, and leave it to the bottom (removing the workspaces and Thunderbird,
  which I not use)
- Mouse setup: enable touchpad click, natural scrolling and increase acceleration
- Disable screensaver, and make windows be selected when mouse moves over them
- Change the terminal shorcuts to change and move tabs (I got used to the KDE shortcuts and never
  bothered in learning the GNOME ones)
- Change the default search engine in Firefox to `DuckDuckGo <https://duckduckgo.com/>`_.
- Set up couple of aliases in `~/.bashrc`: ``alias rgrep="grep -R"`` and ``alias vi="vim"`` (which
  doesn't seem to be required anymore)
- Set up `vim` for Python (and remove some unwanted features like folding)::

   syntax on
   set number
   set autoindent
   set expandtab
   set shiftwidth=4
   set tabstop=4
   set nofoldenable

   execute pathogen#infect()
   set statusline+=%#warningmsg#
   set statusline+=%{SyntasticStatuslineFlag()}
   set statusline+=%*
   let g:syntastic_always_populate_loc_list = 1
   let g:syntastic_auto_loc_list = 0
   let g:syntastic_check_on_open = 1
   let g:syntastic_check_on_wq = 0

Installing software
-------------------

Quite happy with the software that comes preinstalled with Fedora, but few things left to install.
First adding `RPM Fusion <https://rpmfusion.org>`_ repositories::

   sudo dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm

Then updating the system::

   sudo dnf update

Then installing the development group::

   sudo dnf groupinstall "Development Tools"

Also installing all the missing packages (or not missing, but had this list for some years now)::

   sudo dnf install vim-enhanced git vlc gimp inkscape unzip

And finally installing `Miniconda <https://conda.io/miniconda.html>`_. I prefer Miniconda over
Anaconda, because I don't like to have any package in the base environment. So, in every
environment I'm sure there are the packages I'm using (and it's not falling back to the base
environment version, which can be different of the expected).

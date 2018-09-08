Title: Assigning yourself to a GitHub issue
Author: Marc
Date: 2017-10-13 21:30:00
Slug: assigning-yourself-to-github-issue
Tags: 

Contributing to open source is one of the most rewarding experiences one can find. Just finding a bug or a new cool feature of a widely used library, working on it, and sharing it with the rest of the users. This is how open source has become so great and so widely used.

The workflow just described is relatively simply at a small scale, but can become trickier when many people is working in the same project at the same time.

One idea I have in mind, is to create a macro-sprint, where many Python user groups of all around the world sprint on improving [Pandas](https://github.com/pandas-dev/pandas) documentation. Pandas documentation isn't bad, but it could easily be improved by adding more examples to the DataFrame and Series methods for example. An example of page that could be improved by adding examples is the [Series rmul method](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.rmul.html#pandas.Series.rmul).

To organize this, every sprinting team could get a subset of methods. For example, one of the teams could work on the [Series conversion methods](https://pandas.pydata.org/pandas-docs/stable/api.html#conversion). This is a bit tricky, but even with a simple online spreadsheet with all the method categories, we could assign each to a group.

Then, in a sprint with 20 people, working in the same methods, we would create another spreadsheet with each method, and every programmer could assign himself to the method he wants to work on. So, nobody else works on it, which would end up in a lot of wasted time and duplicated work.

But of course, this is very tricky. In a coordinated sprint, working on something very structured like Pandas methods could work. But sounds ridiculous that each project has a spreadsheet with the list of issues, so every programmer can let the others know what she or he is working on.

This was a solved problem 10 years ago when I was quite involved with the [Django](https://www.djangoproject.com/) community. At that time, Django was using [Trac](https://trac.edgewall.org/) to manage the tickets. And every ticket had an "Assigned to" field, where a programmer could let others know that they shouldn't work on it without talking to her or him first.

What is this an issue today? While there are few companies that did as much as [GitHub](https://github.com/) for the open source community, I think they made a big mistake. GitHub also has the "Assigned to" field, but this can only be edited by core developers of the project.

Core developers are surely one of the bottlenecks of every open source community. Coming back to Pandas, there are at the time of writing this post, 100 open pull requests. So, it doesn't seem a good idea, that every time you want to work on an issue, you need to bother a core developer, so she or he assigns the ticket to you.

Is this affecting the open source community? It's difficult to tell, but if we compare the number of assigned tickets in Pandas and Python, we can see how Pandas has 2,039 open issues, but only 30 of them are assigned (I bet all them to core developers).

In comparison, if we check the [Python bug tracker](https://bugs.python.org/)&nbsp;(Python uses GitHub for the code, but not for the issues), we can see that around 50% of the tickets seem to be assigned to someone.

It's difficult to tell what's the effect in code contributions, besides in ticket assignment, but it's reasonable to think that GitHub is discouraging users from contributing, by not letting them assign issues to themselves.

As shown in this [thread](https://github.com/isaacs/github/issues/100), npm creator requested this feature in 2013. 4 years later, there are many +1's in this unofficial ticket (it's not a ticket for GitHub developers, it's for the creator of npm himself, to keep track of his request to GitHub). But the feature is still missing.

Why GitHub is against, or has no interest, in a feature so obviously needed to have a healthy open source community is a mystery to me. But if you feel like I feel, please let [GitHub support](https://github.com/contact) know.
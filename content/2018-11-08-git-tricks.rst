Useful git commands
###################

While `git` is surely one of my favorite tools, and increases my productivity
in a sometimes unbelivable way (like when working on 3 or 5 features at the
same time), some times there are operations that can be a bit tricky.

There are plenty of git tutorials and guides to get started and that explain
the basic concepts. This post is not one of them. If that is what you need,
you can check these great resources:

- `git - the simple guide <http://rogerdudler.github.io/git-guide/>`_
- `Git is a Directed Acyclic Graph and What the Heck Does That Mean?
  <https://medium.com/girl-writes-code/git-is-a-directed-acyclic-graph-and-what-the-heck-does-that-mean-b6c8dec65059>`_
- `Think Like (a) Git <http://think-like-a-git.net/>`_
- `Official documentation <https://git-scm.com/doc>`_

There is another quite popular resource, that doesn't focus on explaining
the concepts, but on what to do if you get into certain cases (aka problems):

- `Oh shit,git! <http://ohshitgit.com/>`_

More on the style of the latter, in this post I'll explain some operations
that are somehow advanced, I don't think are well known, but I use them
frequently. So, hopefully they can be useful to others.

I've got some cool changes, but my history is a mess
----------------------------------------------------

There are many reasons why this can happen. The one that I encounter most
frequently is people opening a pull request, that does not only contain
the user changes (and possibly some merges from master), but instead it
contains commits from other users in the branch, as if they were part of
the pull request. I never spent the time to research what is the cause, but
this is what I usually recommend or do.

Whether it is the previous case, or because of any other reason, if you have
some changes in your branch mixed with a messy git history, the easiest
way I know to go back to a state under control is:

- ``git fetch upstream``: Just updating our local repository.
- ``git merge upstream/master``: Getting anything in the latest repository
  version into our branch.
- ``git reset --soft upstream/master``: This will make that the git history
  in our branch is exactly as the one in master, replacing our messy history.
  And it will leave in our staging area all the changes that we made, compared
  to master.
- ``git commit -m "All my changes in a single commit"``

Now the history in our branch will be equivalent as if we just created
the branch from the latest version, and added a single commit with all our
changes. As usual, we shouldn't rewrite the history if someone else pulled
our commits. But if this is a local branch, or it is remote but only used
to open a pull request, that should be all right.

I have changes in the working directory, and I want to change branch
--------------------------------------------------------------------

There are also different cases for this. The simplest case (but not
common in my case) is that you are working in a branch, and want to
go to make some changes to a different one, but your current changes are
not in a state that you want to commit.

The other cases (the ones that happen to me in practice) are:

- You start working in some changes, and you realize that you are in the
  wrong branch.
- You are making some last minute addition to a pull request, and before
  you commit and push, the pull request is merged. So, you want to continue
  the work in a new branch.

The problem is that when you have uncommitted changes in your working
directory, and you try to change branch, you get the next error message:
`error: Your local changes to the following files would be overwritten by
checkout` preventing any branch change until you commit those changes.
But committing in the current branch is not what we want.

The solution in this case is ``git stash``. With it, the changes in the
working directory are saved into a stack, and the working directory becomes
clean.  This allows us to freely switch branches, and perform other operations.
Once we have the environment ready, and we are in the branch in which the
stacked changes belong to, then we can simply ``git stash apply``. We will get
the uncommitted changes back to the working directory.

I want to test or edit someone else pull request
------------------------------------------------

This is something that mainly project maintainers do, but that can be useful
for anyone. In general, when someone opens a pull request, the changes are
reviewed, and feedback is provided, both in the GitHub (or similar)
interface. And the author, who already got the branch locally, makes changes
and run the code. But in some cases, it may be useful to get the changes of the
pull request locally, so they can be run, and edited.

One example could be a stale pull request, that was opened many months ago
and that the author is not interesting in updating anymore. But it contains
code, that with few changes, would be nice to get merged.

Git is a distributed system, and there is nothing in git itself that tells
which is the "official" repository, and which are forks. To interact
with other repositories from your local copy, all you need is to set a
remote, fetch the changes, and switch to their branches. This would be
done with the commands:

- ``git remote add <remote-name-for-user-fork> <url-to-user-fork>``
- ``git fetch <remote-name-for-user-fork>``

Now, we already have locally all the data in the repo of the author of the
pull request. Next thing is to checkout the branch used for the pull request.
This can be done with:

- ``git branch <branch-name> --track <remote-name-for-user-fork>/<branch-name>``

Now we have the code in the pull request in our working directory. And we can
run or edit.

GitHub has an option when creating a pull request "Allow edits from
maintainers", that is checked by default. If the author of the pull request
left it checked, then maintainers can push to the pull request branch
after editing it locally. So, the updates are made in the same pull request,
which can be merged when it's ready.

For people that are not maintainers, when the checkbox was unchecked, or when
the fork of the author does not exist anymore, pushing to `origin` (your own
fork), and opening a new pull request is required.

If editing other people branches is something that needs to be done often, it
is probably a good idea to use `hub`, a tool from GitHub. It can be installed
with conda:

- ``conda install -c conda-forge hub``

And then, checking out the branch from a pull request is as simple as:

- ``hub checkout <github-url-of-the-pull-request>``

Which will set up the remotes, and make the branch track the parent, so
changes can be pushed with a simple ``git push`` given the right permissions.

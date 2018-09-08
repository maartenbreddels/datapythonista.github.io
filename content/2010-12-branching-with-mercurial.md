Title: Branching with Mercurial
Author: Marc
Date: 2010-12-25 08:53:00
Slug: branching-with-mercurial
Tags: 

This is a simple guide on how to do simple branching operations in Mercurial.

First of all, let's comment the two different options for branching on Mercurial, and in most distributes source control systems.

First option is to create a clone of the original repository to create a branch. This option can be simpler for the user, which has different directories for every branch, and there are not special operations to switch from one branch to another. Another advantage is that branches can be safely switched when some changes are not yet commited, as every branch is in a different directory.

The second option would be to use Mercurial branching commands, and to keep all branches in the same repository. The main advantage of doing this, is that branches can be distributed when using push and pull operations. This is very important, if different programmers need to work with different branches, or if you want to replicate all branches when synchronizing your code with for example [Google code](http://code.google.com/) or [Bitbucket](https://bitbucket.org/).

This second options is the one I'll cover in this simple guide.

Imagine we have a started repository, with some code, and we never used branching before.

If we perform:

<code>
# hg branches
default                       69:3f5490390a0b
</code>

we can see that we already have a branch named default, that is the one that has all our changesets and code.

Now we want to start working on a new version of our application, but we want to be able to do bugfixing to the application we already deployed. We can do it, creating a new branch on our repository.

Look at this example that creates a new branch named newversion, and we create a new file named newfile on it.

<code>
# hg branch newversion
# touch newfile
# hg add newfile
# hg commit -m "commit on the new branch newversion"
</code>

After this, if we check for the branches again, we'll have this:

<code>
# hg branches
newversion                    70:720062b481d7
default                       69:3f5490390a0b (inactive)
</code>

After working on the new branch, we find a bug on the deployed version, and we want to fix it on the version that is deployed. So we have to switch to the default branch to see the content of this branch in our repository directory. We can get it by simply typing:

<code>
# hg update default
# > bugfixedfile
# hg add bugfixedfile
# hg commit -m "bug fixed in default branch"
</code>

NOTE, that we shouldn't have files that are not under the control version system, and that are specific to a branch in the code, as Mercurial will keep those files on the new branch after switching. We can use the option -C if the files are temporary and we want to clear them.

To know the current branch, we can use branch command with no parameters:

<code>
# hg branch
default
</code>

After fixing the bug in the default branch, we'll probably want to fix it in the new version too, so we'll proceed by:

<code>
# hg update newversion
# hg merge default
# hg commit -m "merged from branch default"
</code>

After the new version is ready to be deployed, we'll probably want to merge it back to default, so default will go on being the deployed version. It's recommended to have all changes to the default branch merged to the new version branch, before merging it back to default.

<code>
# hg update newversion
# hg merge default
# hg commit -m "merged from branch default"

# hg update default
# hg merge newversion
# hg commit -m "merged branch newversion into default"
</code>

Finally, the last thing we would want to do is to close the branch where we developed the new version, as further changes to this version will be made to the default branch. It's as simple as:

<code>
# hg update newversion
# hg commit --close-branch -m "closing branch newversion after being merged to default"
</code>
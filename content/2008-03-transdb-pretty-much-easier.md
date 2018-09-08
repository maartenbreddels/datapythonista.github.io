Title: TransDb: Pretty much easier
Author: Marc
Date: 2008-03-06 19:49:00
Slug: transdb-pretty-much-easier
Tags: Applications,Django,IT

Today I've released a new version of TransDb, the Django package that allows storing text at database in more than one language (using the same field).<br/><br/>New version is pretty much easier to use, after fixing many bugs, and avoiding the use of a filter in templates.<br/><br/>Now, migrating your single-language application to a multi-language one is very easy, so almost the only thing you've to do is changing your model fields (no data transformation is required, it is done automatically when you translate texts at admin). A full migration procedure is available at project page.<br/><br/>You can find everything at [Google's project page](http://code.google.com/p/transdb).
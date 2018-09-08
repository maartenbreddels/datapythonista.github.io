Title: Debugging with PDB and App Engine
Author: Marc
Date: 2010-12-04 23:48:00
Slug: debugging-with-pdb-and-app-engine
Tags: Google App Engine

Python debugger (pdb) doesn't work on App Engine SDK as usual. After adding to my project:

<code>
import pdb; pdb.set_trace()
</code>

I got:

<code>
Blocking access to skipped file "<my_path>/.pdbrc"

File "/usr/lib/python2.6/bdb.py", line 46, in trace_dispatch
    return self.dispatch_line(frame)
File "/usr/lib/python2.6/bdb.py", line 65, in dispatch_line
    if self.quitting: raise BdbQuit
</code>

But, as posted in [morethanseven](http://morethanseven.net/2009/02/07/pdb-and-appengine.html), it's easy to make it work using:

<code>
import pdb 
import sys 
for attr in ('stdin', 'stdout', 'stderr'):
    setattr(sys, attr, getattr(sys, '__%s__' % attr))
pdb.set_trace()
</code>
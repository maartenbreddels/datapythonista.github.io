Title: Restrict multiple simultaneos executions of a Python program
Author: Marc
Date: 2009-03-06 15:52:00
Slug: restrict-multiple-simultaneos
Tags: Python

Here you've a simple function to avoid a python script to be executed more than once at the same time:

<code>
def use_lock(func, lockfile):
    if not os.path.exists(lockfile):
        with open(lockfile, 'w') as f:
            f.write(str(os.getpid()))
        func()
        os.remove(lockfile)
        return True
    else:
        return None
</code>

To execute a function main() using a lock file "/var/run/myprogram.pid" just write:

<code>
use_lock(main, '/var/run/myprogram.pid')
</code>

Hope you find it useful.
Title: Building RPMs for Python3.1
Author: Marc
Date: 2011-06-11 20:48:00
Slug: building-rpms-for-python31
Tags: Python

While it's been a long time since the first stable version Python 3 was released, it's not yet available on several operating systems. Looking for a repository with Python 3 rpms, I found [IUS Community](http://iuscommunity.org/Repos), but I had some problems with it, and I thought on building my own rpms.

The process for building an rpm from a source tarball is pretty easy (if you know the steps). The only problem in this case, is that the .spec file delivered with Python is not updated, so the process fails.

I did required changes to the .spec file, and I uploaded it to: [http://files.vaig.be/python-3.1.spec](http://files.vaig.be/python-3.1.spec) (NOTE, that is necessary to edit the exact version of Python you're building in line 37. Version in uploaded file is 3.1.3, but it could be changes to 3.1.3, 3.1.4rc1,...).

Next, you can find the steps for creating a RPM package for Python 3.1 on a CentOS 5 (using my custom .spec file):

<code>
# Install required software
yum install rpm-build gcc expat-devel db4-devel gdbm-devel sqlite-devel ncurses-devel readline-devel zlib-devel openssl-devel

# Download Python source
cd /usr/src/redhat/SOURCES/
wget http://www.python.org/ftp/python/3.1.3/Python-3.1.3.tar.bz2

# Download .spec (rpm specifications file)
cd /usr/src/redhat/SPECS/
wget http://files.vaig.be/python-3.1.spec

# Generate RPMs (and SRPMs)
rpmbuild -ba /usr/src/redhat/SPECS/python-3.1.spec
</code>

Compiling Python and creating the RPM will take a while, but after this process, you'll have the RPMs at:

<code>
/usr/src/redhat/SRPMS/python3.1-3.1.3-1pydotorg.src.rpm
/usr/src/redhat/RPMS/<YOUR-ARCH>/python3.1-3.1.3-1pydotorg.i386.rpm
/usr/src/redhat/RPMS/<YOUR-ARCH>/python3.1-devel-3.1.3-1pydotorg.i386.rpm
/usr/src/redhat/RPMS/<YOUR-ARCH>/python3.1-tools-3.1.3-1pydotorg.i386.rpm
</code>
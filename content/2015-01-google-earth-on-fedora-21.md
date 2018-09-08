Title: Google Earth on Fedora
Author: Marc
Date: 2015-01-19 01:58:00
Slug: google-earth-on-fedora-21
Tags: 

<p>Installing Google Earth in Fedora is trickier than it should. Here is a short HOWTO:</p> - <li>Download 64bits Fedora version from [Google Earth site](https://www.google.com/earth/download/ge/agree.html)</li><li>sudo yum install google-earth-stable_current_x86_64.rpm</li><li>OOOPS!!! You got **file /usr/bin from install of google-earth-stable-7.1.2.2041-0.x86_64 conflicts with file from package filesystem-3.2-28.fc21.x86_64**</li>
  <p>rpm has an error, we need to fix it. We'll rebuild the rpm fixing the error with **rpmrebuild**</p> - <li>sudo yum install rpmrebuild</li><li>rpmrebuild -ep google-earth-stable_current_x86_64.rpm</li><li>A text editor with the spec file (rpm configuration file) is opened, you need to delete the line **%dir %attr(0755, root, root) "/usr/bin"**</li><li>rpmrebuild will ask for confirmation and inform about the path of the generated rpm, just install it</li><li>sudo yum localinstall ~/rpmbuild/RPMS/x86_64/google-earth-stable-7.1.2.2041-0.x86_64.rpm</li>
 <p>Now, the application is succesfully installed, but sometimes crashes when started. It looks like the best to it is to install the 32 bits verion, or Google Earth 6 (latest is 7 at the time of writing this post). Unless you need any specific feature from version 7 I recommend installing version 6 rather than the 32 bits version of 7. The latter requires many dependencies, and it's still buggy on Fedora.</p>  <p>More info:</p>- <li>[https://code.google.com/p/earth-issues/issues/detail?id=1525](https://code.google.com/p/earth-issues/issues/detail?id=1525)</li>

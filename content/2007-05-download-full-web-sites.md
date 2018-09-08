Title: Download full web sites
Author: Marc
Date: 2007-05-05 20:37:00
Slug: download-full-web-sites
Tags: Applications,IT

I've spent too much time searching for an application that allows me downloading all files (all pages, images...) from a web site.<br/><br/>It has been a hard search, but finally I've found one installed on my computer...<br/><br/>Yeah, of course wget can do that! Just use it with few parameters...<br/><br/><span style="font-weight: bold">wget -r -l0 -p</span><br/><br/>And that's all.<br/><br/><strong>UPDATE:</strong> Also very interesting for downloading many files from an ftp server <strong>wget -r --no-passive-ftp ftp://user:password@host/directory</strong> and very interesting <strong>wput</strong> for uploading the files.
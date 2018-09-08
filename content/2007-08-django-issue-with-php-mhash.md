Title: Django issue with PHP mhash
Author: Marc
Date: 2007-08-03 13:17:00
Slug: django-issue-with-php-mhash
Tags: Applications,Django,IT

After installing django, and running with apache, next error could appear:<br/><br/><strong>Looks like your browser isn't configured to accept cookies. Please enable cookies, reload this page, and try again.</strong><br/><br/>It is possible that actually you browser isn't configured to accept cookies, but it is also possible that your apache server is running with PHP support with mhash module enabled; then it is an unsolved and known issue.<br/><br/>This issue causes python md5 module to get unexpected results, when executed in same apache server than mhash PHP module. [Here](http://mail-archives.apache.org/mod_mbox/httpd-python-dev/200706.mbox/%3C27092147.1183094044465.JavaMail.jira@brutus%3E) it is a more detailed description.<br/><br/>It seems to be no solution for that (just uninstall mhash module, or whole php support if possible).
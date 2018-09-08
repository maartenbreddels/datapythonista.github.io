Title: DSNP (Django Start New Project)
Author: Marc
Date: 2007-10-14 22:10:00
Slug: dsnp-django-start-new-project
Tags: Applications,DSNP,Django,IT

[DSNP](http://code.google.com/p/dsnp) is a shell script that automatically creates Django's new projects.<br/><br/>Django is a powerful framework, mostly designed for big applications, but many people uses it for developing little (and many) projects. DSNP eases creation of new projects, automating repetitive steps, and standardizing projects.<br/><br/>Additionally to creating Django's files and directories, DSNP can create a database (and a user) for your project, and can setup apache with necessary changes.<br/><br/>DSNP skeleton consists on next:<br/>.<br/>./public<br/>./public/js<br/>./public/js/admin<br/>./public/css<br/>./public/img<br/>./public/img/admin<br/>./public/model_data<br/>./private<br/>./private/www<br/>./private/www/templates<br/><br/>DSNP doesn't need an installation, just edit dsnp.sh, customize parameters with your preferences, and execute.
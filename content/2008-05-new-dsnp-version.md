Title: New DSNP version
Author: Marc
Date: 2008-05-07 03:46:00
Slug: new-dsnp-version
Tags: Applications,Django,IT

[DSNP](http://code.google.com/p/dsnp/) is a simple and customizable Python script, that automatically creates a working Django project.<br/><br/>Project (and application) creation in Django are very openend and flexible, but sometimes is useful getting all the work done for you, specially:<br/>- <br/>	<li>If you create many Django projects with the same structure.</li><br/>	<li>If you're new to Python, and want to see a "hello world!"  application working in less than one minute.</li><br/>	<li>If you want to check your Django structure with somebody's else (me).</li><br/>
<br/>DSNP does exactly that, automates the process of creating projects and applications in Django. The resulting website is a simple project with a single application, ready for start creating models and templates. It's also customizable, to let everyone set their own preferences in the script, and adapt it to your desired structure.<br/><br/>Want to try it (in five simple steps)?<br/><br/><em>svn checkout http://dsnp.googlecode.com/svn/trunk/</em><br/><em>python dsnp.py myproject</em><br/><em>cd myproject</em><br/><em>python manage.py runserver</em><br/><em>Browse [http://localhost:8000/ ](http://localhost:8000/)</em><br/><br/>Easy right?
Title: DSNP 0.9 released
Author: Marc
Date: 2008-05-10 04:39:00
Slug: dsnp-09-released
Tags: Applications,Django,IT

I know that it was just few days ago that I released another version of DSNP, but because of it, I got a lot of feedback on it, I worked hard, and finally DSNP is stable.<br/><br/>For now, it'll be 0.9 because it works on Django newforms-admin branch, so 1.0 will be reached when newforms-admin will be merged into trunk.<br/><br/>Changeset for this version is next:<br/>- <br/>	<li>Generated sqlite file has write permissions for all users by default</li><br/>	<li>Static files are served by Django http server on development environment (DEBUG==True)</li><br/>	<li>File admin.py created to specify admin options</li><br/>	<li>Media path has changed (now, all static files are under "media" directory) due to an [issue](http://vaig.be/2008/05/09/unable-to-define-my-urls-exactly-my-way-resignation-statement/)</li><br/>
<br/>I hope you like it.
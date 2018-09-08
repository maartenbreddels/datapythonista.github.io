Title: StdImageField: Improved image field for Django
Author: Marc
Date: 2008-05-17 03:23:00
Slug: stdimagefield-improved-image-field-for
Tags: Applications,Django,IT

I'm pleased to announce a new project, [django-stdimage](http://code.google.com/p/django-stdimage/), that provides a new image field with many improvements respect to Django's core ImageField.<br/><br/>Features of StdImageField:<br/>- <br/>	<li>Saved files have standardized names (using field name and object id)</li><br/>	<li>Images can be removed</li><br/>	<li>Automatically creates a thumbnail</li><br/>	<li>Automatically resizes both image and thumbnail (with optional crop to fit exactly specified size)</li><br/>
<br/>Here you've an example of usage:<br/><br/><code><br/>from django.db import models<br/>from stdimage import StdImageField</code><br/><code><br/>class MyClass(models.Model):<br/>&nbsp;&nbsp;my_image = StdImageField(upload_to='path/to/img', blank=True, \<br/>&nbsp;&nbsp;&nbsp;&nbsp;size=(640, 480), thumbnail_size=(100, 100, True))</code><br/><br/>If a file called "uploaded_file.png" is uploaded for object id 34, then result will be:<br/>- <br/>	<li> /path/to/img/my_image_34.png (with bigger possible size to fit in a 640x480 area)</li><br/>	<li>/path/to/img/my_image_34.thumbnail.png (with a exact size of 100x100, cropping if necessary)</li><br/>
<br/>Also it will appear a check-box for deleting when using admin.
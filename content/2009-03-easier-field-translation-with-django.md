Title: Easier field translation with django-transmeta
Author: Marc
Date: 2009-03-04 11:44:00
Slug: easier-field-translation-with-django
Tags: Django

[django-transmeta](http://code.google.com/p/django-transmeta) is a new project that provides django field translations in a simpler way than existing ones like [django-multilingual](http://code.google.com/p/django-multilingual/) and [transdb](http://code.google.com/p/transdb/).

The basis of that simplicity is creating a field in the database table for every translation, so internally we'll have something like:

<code>
CREATE TABLE app_model (
&nbsp;&nbsp;&nbsp;&nbsp;[...]
&nbsp;&nbsp;&nbsp;&nbsp;myfield_en varchar,
&nbsp;&nbsp;&nbsp;&nbsp;myfield_ca varchar,
&nbsp;&nbsp;&nbsp;&nbsp;[...]
);
</code>

where "en" and "ca" are the languages in our application (English and Catalan in this case).

For the developer, translating a model is as simple as adding a metaclass to the model, and specify the fields to translate in its Meta class:

<code>
from transmeta import TransMeta

class MyModel(models.Model):
&nbsp;&nbsp;&nbsp;&nbsp;`__metaclass__` = TransMeta

&nbsp;&nbsp;&nbsp;&nbsp;name = models.CharField(max_length=64)
&nbsp;&nbsp;&nbsp;&nbsp;description = models.TextField()
&nbsp;&nbsp;&nbsp;&nbsp;price = models.FloatField()

&nbsp;&nbsp;&nbsp;&nbsp;class Meta:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;translate = ('name', 'description', )
</code>

Even with this project is still as tricky as transdb and multilingual, its main goal is being really really simple, for its design, for developers, and its code (that mainly it's about 120 lines of code). It also breaks some limitations of transdb (its most simple predecessor IMHO) like translating non-text fields.

I also want to mention that I just discovered a new project for translating model fields, named [django-modeltranslation](http://code.google.com/p/django-modeltranslation), that looks cool, but I don't like the (admin like) registering way to set translatable fields (too much complicated).
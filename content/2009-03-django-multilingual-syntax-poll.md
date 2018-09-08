Title: django-multilingual syntax poll
Author: Marc
Date: 2009-03-10 00:00:00
Slug: django-multilingual-syntax-poll
Tags: Django

Those days there is some activity in the django model translation area, specially for the two new projects that joined [django-multilingual](http://code.google.com/p/django-multilingual/) and [transdb](http://code.google.com/p/transdb/) to achieve this: [django-transmeta](http://code.google.com/p/django-transmeta) and [django-modeltranslation](http://code.google.com/p/django-modeltranslation/).

While there are some intentional differences among some projects (for example django-modeltranslation is the only one that can translate models without editing them), it would be great to merge all (or most) existing projects, and join the efforts to get our best application (and hopefully it'll worth to be included in Django itself).

So, with the merge of those applications in mind, we're [planning](http://groups.google.com/group/django-multilingual/browse_thread/thread/2fab1d1674090079) to create a branch on django-multilingual that will have the very best of each existing application, and any other cool idea.

So if you have good Python/Django skills, and want to add some open source work in your CV... ;)  join us now!

Or if you are a potential user of this application, or you just think that your opinion is worth to be shared, please fill the [<span style="font-weight:bold;">MODEL SYNTAX POLL</span>](http://doodle.com/aicvayf8ss2mxm2h), or mail [us](http://groups.google.com/group/django-multilingual/browse_thread/thread/2fab1d1674090079) with your ideas.

Here there are simple sample for each option on the poll:

class Translation

    ::::
    
    class MyModel(model.Model):
        my_field = CharField()
    
        class Translation(multilingual.Translation):
            my_i18n_field = CharField()
    


custom fields

    ::::
    
    class MyModel(model.Model):
        my_field = CharField()
        my_i18n_field = TransCharField()
    


separate model

    ::::
    
    class MyModel(model.Model):
        my_field = CharField()
        my_i18n_field = CharField()
    
    Class MyModelTranslation(TranslationOptions):
        fields = ('my_i18n_field',)
    


translate attrs in Meta

    ::::
    
    class MyModel(model.Model):
        my_field = CharField()
        my_i18n_field = CharField()
    
        class Meta:
            translate = ('my_i18n_field',)
    


translate=True in field options

    ::::
    
    class MyModel(model.Model):
        my_field = CharField()
        my_i18n_field = CharField(translate=True)
    
    


Do you have a better idea?
Just leave a comment here,
or write a mail on this [thread](http://groups.google.com/group/django-multilingual/browse_thread/thread/2fab1d1674090079)
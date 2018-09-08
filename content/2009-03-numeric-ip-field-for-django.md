Title: Numeric IP field for Django
Author: Marc
Date: 2009-03-06 13:05:00
Slug: numeric-ip-field-for-django
Tags: Django

Some time ago I needed to add an IP field to my model with more records (some hundred thousands). I was going to just add Django's IPAddressField, but I realized that it stores the data as text on the database, and I didn't like the idea.

Basically, and IP address is just 4 bytes of data, but it's text representation can use between 7 and 15 bytes. That's not a big different when your model will have few rows, but it's a different when you'll have a huge set of IP addresses, and specially if you want to join tables by it.

The only inconvenient of storing the IPs as numbers is that are not human readable if you want to check them directly to database.

So, here you have my code that can be used as a replacement of IPAddressField:


    ::::
    
    import IPy 
    from django.db import models
    from django import forms
    from django.utils.translation import ugettext as _
    
    def _ip_to_int(ip):
        return IPy.IP(ip).ip
    
    def _int_to_ip(numeric_ip):
        return IPy.IP(numeric_ip).strNormal()
    
    class IPFormField(forms.fields.Field):
        def clean(self, value):
            try:
                _ip_to_int(value)
            except ValueError:
                raise forms.ValidationError, \
                    _('You must provide a valid IP address')
    
            return super(IPFormField, self).clean(value)
    
    class IPField(models.fields.PositiveIntegerField):
        ''' 
        IP field for django for storing IPs as integers on database
        (Django's field IPAddressField stores them as text)
        '''
        __metaclass__ = models.SubfieldBase
    
        def to_python(self, value):
            if value:
                if isinstance(value, long):
                    return _int_to_ip(value)
                else:
                    return value
            else:
                return None
    
        def get_db_prep_save(self, value):
            try:
                result = _ip_to_int(value)
            except ValueError:
                result = None
            return result
    
        def get_db_prep_value(self, value):
            if value:
                return _ip_to_int(value)
            else:
                return None
    
        def get_db_prep_lookup(self, lookup_type, value):
            return super(IPField, self).get_db_prep_lookup(
                lookup_type,
                _ip_to_int(value)
            )   
    
        def formfield(self, **kwargs):
            defaults = {'form_class': IPFormField}
            defaults.update(kwargs)
            return super(IPField, self).formfield(**defaults)
    
    


<span style="font-weight:bold;">NOTE</span>: This code requires [IPy](http://c0re.23.nu/c0de/IPy/), a single file python library to work with IP addresses.
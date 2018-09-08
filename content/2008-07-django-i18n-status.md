Title: Django i18n status
Author: Marc
Date: 2008-07-26 04:11:00
Slug: django-i18n-status
Tags: Applications,Django,IT

<p>Here you have what, from my point of view, is the status of django i18n. Comments will be very welcome, specially from people from countries with other i18n needs than mine (based on the idea that Django i18n is perfect for people in the US, here is the troubleshooting for my country, for sure more problems exists for people in for example China).</p>
<p>This list is part of the analysis that I'm doing to fix all those problems. If you want to participate in making Django also "The web framework for perfectionists outside the US", please contact me.</p>
<table border="0">
<tbody><tr>
<td><strong>Subject</strong></td>
<td><strong>
</strong></td>
<td><strong>Comments</strong></td>
<td>
</td>
</tr>
<tr>
<td>Translation (static content)</td>
<td style="background-color: rgb(127, 255, 0);">Yes</td>
<td>Django has an amazing translation system, easy to use, and exceptionally automated. Also it has bidi support. Despite of this, some problems can be found when translating django or applications to other languages (masculine/femenine...).</td>
<td>
</td>
</tr>
<tr>
<td>Translation (database content)</td>
<td style="background-color: rgb(220, 20, 60);">No</td>
<td>Django doesn't support model field translation, but it can be achieved using an external application such as [TransDb](http://code.google.com/p/transdb/), [django-multilingual](http://code.google.com/p/django-multilingual/), [django-utils](http://code.google.com/p/django-utils) translation service and [i18ndynamic](http://code.google.com/p/i18ndynamic/). As far as I know only TransDb and django-multilingual are working on Django's trunk.</td>
<td>
</td>
</tr>
<tr>
<td>Calendar customization</td>
<td style="background-color: rgb(220, 20, 60);">No</td>
<td>Patching Django is required to change first day of week in admin calendar (first day of week is Monday according to ISO and in many countries (most Europe, most South America, and some parts of Asia). See ticket [#1061](http://code.djangoproject.com/ticket/1061)</td>
<td>
</td>
</tr>
<tr>
<td>Date format (when displaying)</td>
<td style="background-color: rgb(127, 255, 0);">Yes</td>
<td>Dates displayed in admin are formatted according to current locale. Also custom dates can be easily formatted using date filter (f.e. {{ my_date|date:_("DATE_FORMAT") }} ).

The problem here, is that few internationalized formats are defined inside django, so using django formats you can internationalize a date with format "December 31th, 2000", but not with format "12/31/2000". It can be achieved creating date formats in your catalog.</td>
<td>
</td>
</tr>
<tr>
<td>Date format (on inputs)</td>
<td style="background-color: rgb(220, 20, 60);">No</td>
<td>Django allows specifying one or many input formats for a date form field (using the input_formats parameter of the form field).I think that there is no way to specify the format on the admin fields, specially because the format that generates the calendar is always the same.

Anyway what it's expected is not to specify the format of a field, actually it is to get the format from the current locale.</td>
<td>
</td>
</tr>
<tr>
<td>Number format (when displaying)</td>
<td style="background-color: rgb(220, 20, 60);">No</td>
<td>Django has just a filter (floatformat) to format numbers, where you can specify how many decimals you want. It's very difficult to customize your number format, to the format of the current locale, and even to a fixed format.</td>
<td>
</td>
</tr>
<tr>
<td>Number format (on input)</td>
<td style="background-color: rgb(220, 20, 60);">No</td>
<td>Django has no way to specify if you want to enter a decimal number with comma separator (dot is always used). Of course it can't be done according to current locale.</td>
<td>
</td>
</tr>
</tbody></table>
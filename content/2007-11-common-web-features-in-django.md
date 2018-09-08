Title: Common web features in Django
Author: Marc
Date: 2007-11-11 02:30:00
Slug: common-web-features-in-django
Tags: Applications,Django,IT

Here is a brief list of common web features, and the best way I know for achieving it in Django:<br/>- <br/>	<li><strong>Breadcrumbs:</strong> use {{ block.super }} for recursive link inheritance [[more info](http://www.martin-geber.com/weblog/2007/10/25/breadcrumbs-django-templates/)]</li><br/>	<li><strong>Back button:</strong> use {{ request.META.HTTP_REFERER }} for linking to referring URL*</li><br/>	<li><strong>Highlight active menu option:</strong> use {{ request.path }} to know requested URL and compare it with menu options * [[more info](http://gnuvince.wordpress.com/2007/09/14/a-django-template-tag-for-the-current-active-page/)]</li><br/>	<li><strong>Pagination:</strong> use 'django.views.generic.list_detail.object_list' generic view [[more info](http://www.djangoproject.com/documentation/generic_views/#django-views-generic-list-detail-object-list)]</li><br/>
<br/>* it's needed to add 'request' module to [TEMPLATE_CONTEXT_PROCESSORS](http://www.djangoproject.com/documentation/settings/#template-context-processors) on settings.py
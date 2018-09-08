#!/usr/bin/env python
AUTHOR = 'Marc Garcia'
SITE_LOGO = '../static/img/profile.png'
SITENAME = 'datapythonista blog'
SITESUBTITLE = 'about me'
SITEURL = '/blog'
OUTPUT_PATH = 'blog'
PATH = 'content'
TIMEZONE = 'Europe/London'
DEFAULT_LANG = 'English'
THEME = 'attila'
HEADER_COVER = '../static/img/bg.jpg'
MARKUP = ('rst', 'md', 'ipynb')
PLUGIN_PATHS = ['plugins']
# PLUGINS = ['ipynb.markup']
IPYNB_USE_METACELL = True
GOOGLE_ANALYTICS = 'UA-1635939-25'
CSS_OVERRIDE = ['../static/css/blog.css']
JS_OVERRIDE = ['../static/js/blog.js']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 5

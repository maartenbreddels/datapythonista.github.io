#!/usr/bin/env python
AUTHOR = 'Marc Garcia'
SITE_LOGO = '../static/img/profile.png'
SITENAME = 'datapythonista blog'
SITESUBTITLE = 'about me'
SITEURL = 'https://datapythonista.github.io/blog'
OUTPUT_PATH = 'blog'
PATH = 'content'
TIMEZONE = 'Europe/London'
DEFAULT_LANG = 'en'
THEME = 'attila'
HEADER_COVER = '../static/img/bg.jpg'
MARKUP = ('rst', 'md', 'ipynb')
PLUGIN_PATHS = ['plugins']
# PLUGINS = ['ipynb.markup']
IPYNB_USE_METACELL = True
GOOGLE_ANALYTICS = 'UA-1635939-25'
CSS_OVERRIDE = ['../static/css/blog.css']
JS_OVERRIDE = ['../static/js/blog.js']
DISQUS_SITENAME = 'datapythonista'
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'atom.xml'
# Using CATEGORY_FEED_ATOM seems broken
CATEGORY_FEED_ATOM = None  #'{slug}.atom.xml'

DEFAULT_PAGINATION = 5

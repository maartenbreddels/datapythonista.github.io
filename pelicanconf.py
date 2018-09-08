#!/usr/bin/env python
AUTHOR = 'Marc Garcia'
SITENAME = 'datapythonista blog'
SITEURL = '/blog'
OUTPUT_PATH = 'blog'
PATH = 'content'
TIMEZONE = 'Europe/London'
DEFAULT_LANG = 'English'
THEME = 'attila'
HEADER_COVER = '../static/img/bg.jpg'
MARKUP = ('rst', 'md', 'ipynb')
PLUGIN_PATHS = ['plugins']
#PLUGINS = ['ipynb.markup']
IPYNB_USE_METACELL = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

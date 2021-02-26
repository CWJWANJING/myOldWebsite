#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Wanjing Chen'
SITENAME = 'Wanjing Chen'
SITEURL = ''

PATH = 'content'

STATIC_PATHS = ['images', 'pages', 'files']

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

PROFILE_IMAGE='profile.jpg'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PAGE_URL = "{slug}.html"
PAGE_SAVE_AS = "{slug}.html"
ARTICLE_URL = "blog/{slug}"
ARTICLE_SAVE_AS = "blog/{slug}.html"

DISPLAY_PAGES_ON_MENU=True
DELETE_OUTPUT_DIRECTORY = True

# Blogroll
LINKS = (('About', '/about'),
         ('CV', '/pages/cv.pdf'),
         ('Programming Projects', '/programmingprojects'),
         ('UX Projects', '/category/ux')
         )

# Social widget
SOCIAL = (('github', 'https://github.com/CWJWANJING'),
          ('twitter', 'http://twitter.com/wanjingchen')
          )

# Services
GOOGLE_ANALYTICS = 'UA-168444581-1'


DEFAULT_PAGINATION = 5

THEME = 'pelican-hyde'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

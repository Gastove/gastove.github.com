#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
# import pelican_gist

AUTHOR = u'Ross Donaldson'
SITENAME = u'Strangely Specific and Very Odd'
SITEURL = 'http://blog.gastove.com'

THEME = '../lib/theme/svbhack'

USER_LOGO_URL = 'http://www.gravatar.com/avatar/a942cea13e537bb0ea754b6d216c3377?size=160'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = u'en'
DEFAULT_DATE_FORMAT = '%a, %b %d %Y'
DEFAULT_PAGINATION = 5

MARKUP = ('md', 'markdown')
MD_EXTENSSIONS = ['codehilite', 'footnotes']
# PLUGINS = ['pelican_gist']

# Sensible defaults for pelican_gist
GIST_CACHE_ENABLED = True
GIST_CACHE_LOCATION = '../.gist-cache'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Paths
INPUT_PATH = '../content'
OUTPUT_PATH = '../output'

# Blogroll
LINKS =  (('Home', 'http://www.gastove.com'),
          ('Food', 'http://food.gastove.com/'),
#          ('Pelican', 'http://getpelican.com/'),
)

# Social widget
SOCIAL = (('Twitter', 'http://www.twitter.com/Gastove'),
          ('Github', 'http://www.github.com/Gastove'),)

TWITTER_USERNAME = 'gastove'

# Handy Dandy Third Parties
GOOGLE_ANALYTICS = 'UA-43979937-2'
DISQUS_SITENAME = 'veryodd'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ben Glassman'
SITENAME = u'Web 2 (GDD 306) @ Champlain College'
SITEURL = ''

TIMEZONE = 'America/New York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = False

# Social widget
SOCIAL = False

DEFAULT_PAGINATION = 10

THEME = 'themes/champlain'

STATIC_PATHS = ['images', 'materials']

WEBASSETS = True

PLUGIN_PATH = 'plugins'
PLUGINS = ['assets']

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Course Settings
COURSE_NAME = 'Web 2'
COURSE_NUM = 'GDD 306-51'
COURSE_SEMESTER = 'Fall 2014'
COURSE_LOCATION = 'Joyce Hall, Room 103'
COURSE_TIMES = 'Tuesday 5:30 - 8:15 PM'
INSTRUCTOR_NAME = 'Ben Glassman'
INSTRUCTOR_EMAIL = 'bglassmancc@gmail.com'

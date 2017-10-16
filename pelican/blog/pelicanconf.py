#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"The Castle Mountaineering Club."
SITENAME = u"The Castle Mountaineering Club."

# THEME = "../themes/pelican-bootstrap3"
THEME = "/home/ian/pelican-themes/pelican-bootstrap3"
BOOTSTRAP_THEME='readable'
#BOOTSTRAP_THEME = 'readable'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_SIDEBAR = True
DISPLAY_CATEGORIES_ON_SIDEBAR = False
# PAGE_URL(‘pages/{slug}.html’)
#PAGE_PATHS = ('pages')
PAGES_SORT_ATTRIBUTE = 'filename'
PAGE_TITLE=False

TIMEZONE = 'Europe/London'
MARKUP = (('rst', 'md', 'yml'))
DEFAULT_LANG = 'en'

# Blogroll
LINKS =  (('v-g Backpacking', 'http://v-g.me.uk/'),
          ('Footless Crow', 'http://footlesscrow.blogspot.co.uk/'),
          ('Emacs org-mode', 'http://org-mode.org')
          ,)

# Social widget
SOCIAL = ''
DEFAULT_PAGINATION = 10

OUTPUT_PATH = "/home/ian/Documents/emacs/thecastle/pelican/blog/output"

STATIC_PATHS = (['images'])

#NEWEST_FIRST_ARCHIVES (True)

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

ARTICLE_URL = "posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html"

CC_LICENSE = "CC-BY-NC-SA"

GITHUB_URL = "https://github.com/thecastle"


PLUGIN_PATHS = ["/home/ian/src/pelican-plugins"]
PLUGINS = ['summary', 'org_reader', 'i18n_subsites']
READERS = {'org': "org_reader"}
ORG_READER_EMACS_LOCATION = '/usr/bin/emacs'

IGNORE_FILES = ['.~', 'setup.org', 'LICENCE.org', 'TheCastle.org', 'List_of_Photographs.org', 'TheCastle_epub.org']

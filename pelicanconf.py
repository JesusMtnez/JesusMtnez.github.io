#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'JesusMtnez'
SITEURL = ''
SITENAME = 'JesusMtnez\'s Blog'
SITETITLE = 'Blog de Jesús Martínez-B. H.'
SITESUBTITLE = 'Backend Developer'
SITELOGO = '/images/profile.jpeg'
SITEDESCRIPTION = 'Historias de un programador ávido de conocimiento'

I18N_TEMPLATES_LANG = 'en'
DEFAULT_LANG = 'es'
OG_LOCALE = 'es_ES'
LOCALE = 'es_ES.UTF-8'

JINJA_EXTENSIONS = ['jinja2.ext.i18n']
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['i18n_subsites']

PATH = 'content'
OUTPUT_PATH = 'public'
STATIC_PATHS = ['images', 'extra']
TIMEZONE = 'Europe/Madrid'
COPYRIGHT_YEAR = 2017


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (
  ('twitter', 'https://twitter.com/JesusMtnezBH'),
  ('linkedin', 'https://linkedin.com/in/JesusMtnez'),
  ('gitlab', 'https://gitlab.com/JesusMtnez'),
  ('github', 'https://github.com/JesusMtnez')
)

# Theme settings
THEME = "Flex"
PYGMENTS_STYLE = 'native'
DEFAULT_PAGINATION = 10

# Menu settings
MAIN_MENU = True
MENUITEMS = (
  ('Archivo', '/archives.html'),
  ('Categorias', '/categories.html')
)

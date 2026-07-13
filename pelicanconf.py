#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =====================================================================
# CONFIGURACIÓN DE DESARROLLO
# =====================================================================

AUTHOR = 'Amanda Salinas'
# >>> EDITA: el nombre del blog (este es provisional) <<<
SITENAME = 'doting wabisabi'
SITESUBTITLE = 'nothing lasts, nothing is finished, and nothing is perfect'
SITEURL = ""

PATH = "content"
THEME = "theme/tinta"
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'es'

MENUITEMS = (
    ('Poemas', '/category/poemas.html'),
    ('Prosa', '/category/prosa.html'),
    ('Archivo', '/archives/'),
    ('Acerca', '/about/'),
)

ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME':{'path': 'CNAME'}}
DEFAULT_PAGINATION = 8

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

RELATIVE_URLS = True

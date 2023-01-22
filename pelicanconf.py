#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import pelican

AUTHOR = "Jonas Tischer"
SITENAME = "Jonas Tischer"
SITEURL = ""
SITE_DESCRIPTION = (
    "My personal website. "
)
# TODO
PATH = "content"
TIMEZONE = "Europe/Berlin"
DEFAULT_LANG = "en"
THEME = "./theme"
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}.html"
DEFAULT_CATEGORY = "blog"
ARTICLE_URL = "{category}/{slug}.html"
ARTICLE_SAVE_AS = "{category}/{slug}.html"
ARTICLE_EXCLUDES = ["html"]
CATEGORY_URL = "category/{slug}.html"
CATEGORY_SAVE_AS = "category/{slug}.html"
USE_FOLDER_AS_CATEGORY = False

# SEO
PELICAN_VERSION = pelican.__version__

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_ALL_ATOM = "feed.xml"

# NO EXTRAS
TAGS_SAVE_AS = None
ARCHIVES_SAVE_AS = None
CATEGORIES_SAVE_AS = None
AUTHORS_SAVE_AS = None

# pagination
DEFAULT_PAGINATION = False

# extra paths
STATIC_PATHS = [
    "html",
    "extra/favicons",
]
EXTRA_PATH_METADATA = {
    "extra/favicons/": {"path": "favicons/"},
    "html/StateOfVim.html": {"path": "StateOfVim.html"},
}

# MARKDOWN
MARKDOWN = {
    "extensions": [
        "markdown.extensions.toc",
        "markdown.extensions.fenced_code",
        "markdown.extensions.codehilite",
    ]
}

# PLUGINS
PLUGIN_PATHS = ["plugins"]
PLUGINS = [
    "pelican.plugins.sitemap",
    "pelican.plugins.simple_footnotes",
    "pelican.plugins.feed_filter",
]
SITEMAP = {
    "exclude": ["archives.html", "author/", "category/"],
    "format": "xml",
    "priorities": {"articles": 0.9, "indexes": 0.5, "pages": 0.9},
    "changefreqs": {
        "articles": "hourly",
        "indexes": "hourly",
        "pages": "hourly",
    },
}

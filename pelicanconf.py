AUTHOR = "John"
SITENAME = "Susan's Recipe Book"
SITEURL = ""
PATH = 'content'
THEME = '/Users/john/src/github.com/trammell/pelican-mangia'
TIMEZONE = "America/Chicago"
DEFAULT_LANG = "en"
MENUITEMS = (
    ("breakfast dishes","category/appetizers.html"),
    ("dinner dishes","category/dinners.html"),
    ("cocktails","category/cocktails.html"),
    ("see all categories","categories.html"),
    ("book view","book.html"),
)
DISPLAY_PAGES_ON_MENU = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Book configuration
BOOK = {
    'categories': [ 'cocktails' ]
}

# Blogroll
LINKS = (("Source code on GitHub", "https://github.com/trammell/recipe-book"),)

STATIC_PATHS = ["images", "extra"]
EXTRA_PATH_METADATA = {"extra/favicon.ico": {"path": "favicon.ico"}}

# Social widget
SOCIAL = ()
DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

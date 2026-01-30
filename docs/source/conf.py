
project = 'mygithubpages'
copyright = '2026, prevLanky'
author = 'prevLanky'

#templates_path = ['_templates']
#exclude_patterns = []
#extensions = ["ablog", "myst_parser"]  # myst_parser if using Markdown
extensions = [
    'myst_parser',
    'ablog',
    'sphinx.ext.intersphinx',
    'sphinx.ext.extlinks',
    'sphinx.ext.todo',
]
html_static_path = ['_static']


html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    "collapse_navigation": True,  # Makes TOC collapsible
    "sticky_navigation": True,    # Keeps sidebar while scrolling
    "navigation_depth": 4,        # How deep to show nested pages
}
myst_heading_anchors = 3  # generates anchors for H1, H2, H3

# ablog settings
blog_baseurl = "https://prevLanky.github.io/prevLanky.github.io/"
blog_title = "My Blog"
blog_path = "blog"
blog_authors = {"prevLanky": ("prevLanky", "https://github.com/prevLanky")}
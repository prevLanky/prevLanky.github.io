
project = 'mygithubpages'
copyright = '2026, prevLanky'
author = 'prevLanky'

#templates_path = ['_templates']
#exclude_patterns = []
#extensions = ["ablog", "myst_parser"]  # myst_parser if using Markdown
extensions = [
    'myst_parser',
    'sphinx.ext.intersphinx',
    'sphinx.ext.extlinks',
    'sphinx.ext.todo',
    'sphinx_rtd_dark_mode'
]
html_static_path = ['_static']


#html_theme = 'sphinx_rtd_theme'
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    "navigation_depth": 10,        # how deep the sidebar goes
    "navigation_with_keys": True, # optional: allow keyboard navigation
}
myst_heading_anchors = 7
default_dark_mode = True
# ablog settings
#blog_baseurl = "https://prevLanky.github.io/prevLanky.github.io/"
#blog_title = "My Blog"
#blog_path = "blog"
#blog_authors = {"prevLanky": ("prevLanky", "https://github.com/prevLanky")}
project = 'mygithubpages'
copyright = '2026, prevLanky'
author = 'prevLanky'

extensions = [
    'myst_parser',
    'sphinx.ext.intersphinx',
    'sphinx.ext.extlinks',
    'sphinx.ext.todo',
    'sphinx_rtd_dark_mode',
    "sphinx.ext.graphviz"
]

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    "navigation_depth": 10,
    "navigation_with_keys": True,
    "collapse_navigation": False,
    "sticky_navigation": True,
}

html_sidebars = {
    "**": [
        "globaltoc.html",
        "relations.html",
        "sourcelink.html",
        "searchbox.html",
    ]
}

toc_object_entries_show_parents = "all"

html_static_path = ['_static']

myst_heading_anchors = 7
default_dark_mode = True
graphviz_output_format = "png"
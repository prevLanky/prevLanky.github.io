
# Build files
rm -rf docs/build && python -m sphinx -b html docs/source docs/build/html

# Setup github pages
pip install sphinx
pip install furo
mkdir docs
cd docs
sphinx-quickstart
open: docs/source/conf.py
add: html_theme = "furo"
sphinx-build -b html source build/html
git checkout --orphan gh-pages
git rm -rf .
cp -r docs/build/html/* .
touch .nojekyll
Go to Repo → Settings → Pages
Branch: gh-pages
Folder: / (root)


# Build files
rm -rf docs/build && python -m sphinx -b html docs/source docs/build/html

# Setup github pages
# Install/update pip
python -m pip install --upgrade pip

# Install Sphinx and Furo
python -m pip install sphinx
python -m pip install furo
python -m pip install myst-parser sphinx-rtd-theme sphinx-rtd-dark-mode


# Create Sphinx project
sphinx-quickstart
python -m pip install --upgrade pip
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

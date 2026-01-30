
# Build files
python -m sphinx -b html source build/html

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

# create orphan branch
git checkout --orphan gh-pages
# remove all files
git rm -rf .
# make an empty commit
git commit --allow-empty -m "Initialize gh-pages"
# push to GitHub
git push origin gh-pages
# switch back to main
git checkout main
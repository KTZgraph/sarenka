import os
import sys
sys.path.insert(0, os.path.abspath('../sarenka/backend/backend'))

project = 'SARENKA'
copyright = '2021, Dominika Pawlaczyk, Michał Pawlaczyk, Karolina Słonka'
author = '0.0.1'


release = '0.0.1'


extensions = [
    'sphinx.ext.autodoc'
]

html_theme = "sphinx_rtd_theme"


templates_path = ['_templates']


exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_static_path = ['_static']
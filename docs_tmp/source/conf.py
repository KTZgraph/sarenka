import os
import sys
import django
sys.path.insert(0, os.path.abspath('../../sarenka/backend'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'backend.settings.base'
django.setup()

project = 'SARENKA'
copyright = '2021, Dominika Pawlaczyk, Michał Pawlaczyk'
author = '0.0.1'


release = '0.0.1'


extensions = [
    'sphinx.ext.autodoc',
    'sphinxcontrib_django',
    'sphinx.ext.viewcode',
    'sphinx_autodoc_typehints',
    'sphinx.ext.githubpages',
    'sphinx.ext.graphviz',
    'sphinx_autodoc_annotation',
]

html_theme = "sphinx_rtd_theme"


templates_path = ['_templates']


exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_static_path = ['_static']
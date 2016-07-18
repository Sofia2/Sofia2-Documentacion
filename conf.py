# -*- coding: utf-8 -*-
#
import os
import sys

from recommonmark.parser import CommonMarkParser

sys.path.insert(0, os.path.abspath('..'))

sys.path.append(os.path.abspath('_ext'))
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.httpdomain'
]
templates_path = ['_templates']

source_suffix = ['.rst', '.md']
source_parsers = {
    '.md': CommonMarkParser,
}

master_doc = 'index'
project = u'Sofia2'
copyright = u'2017, Indra'
version = '1.0'
release = '1.0'
exclude_patterns = ['_build']
default_role = 'obj'
pygments_style = 'sphinx'
intersphinx_mapping = {
    'python': ('http://python.readthedocs.io/en/latest/', None),
    'django': ('http://django.readthedocs.io/en/latest/', None),
    'sphinx': ('http://sphinx.readthedocs.io/en/latest/', None),
}
# This doesn't exist since we aren't shipping any static files ourselves.
#html_static_path = ['_static']
htmlhelp_basename = 'Sofia2'
latex_documents = [
  ('index', 'test.tex', u'Sofia2',
   u'Indra', 'manual'),
]
man_pages = [
    ('index', 'Sofia2', u'Sofia2',
     [u'Indra'], 1)
]

exclude_patterns = [
    # 'api' # needed for ``make gettext`` to not die.
]

language = 'en'

locale_dirs = [
    'locale/',
]
gettext_compact = False


on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

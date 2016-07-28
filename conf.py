# -*- coding: utf-8 -*-
#
import os
import sys
import json

#from recommonmark.parser import CommonMarkParser
#sys.path.insert(0, os.path.abspath('..'))
#sys.path.append(os.path.abspath('_ext'))

#extensions = ['jsonlexer']
extensions = []
templates_path = ['_templates']

source_suffix = ['.rst', '.md']

master_doc = 'index'
project = u'Sofia2'
copyright = u'2016, Indra'
version = '1.0'
release = '1.0'
exclude_patterns = ['_build']
#default_role = 'obj'
pygments_style = 'sphinx'

# This doesn't exist since we aren't shipping any static files ourselves.
#html_static_path = ['_static']

htmlhelp_basename = 'Sofia2'

latex_documents = [
  ('index', 'Sofia2.tex', u'Sofia2',
   u'Indra', 'manual'),
]
man_pages = [
    ('index', 'Sofia2', u'Sofia2',
     [u'Indra'], 1)
]
#language = 'en'


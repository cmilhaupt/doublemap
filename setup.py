#!/usr/bin/env python
from setuptools import setup, find_packages

setup  (
    name        = 'doublemap',
    version     = '0.0.1',
    description = 'An API client for DoubleMap with useful route tracking utilities',
    author = 'Travis Cunningham',
    author_email = 'travcunn@umail.iu.edu',
    url = 'https://github.com/travcunn/doublemap',
    license = 'MIT',
    packages  =  find_packages('src'),
    package_dir = {'' : 'src'}
)

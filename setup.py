#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name         = 'freud',
    version      = '0.1',
    description  = 'Client-Specific Equivalence Checking of Python Programs',
    author       = 'Federico Mora',
    author_email = 'fmorarocha@gmail.com',
    url          = 'https://github.com/Client-Specific-Equivalence-Checker/freud-tool',
    scripts      = ['bin/freud'],
    packages     = find_packages(),
    package_dir  = {'freud': 'freud'},
    install_requires=[
        'pyexsmt>=0.1'
    ]
)

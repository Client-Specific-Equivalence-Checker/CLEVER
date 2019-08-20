#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name         = 'CLEVER',
    version      = '0.1',
    description  = 'Client-Specific Equivalence Checking of Python Programs',
    scripts      = ['bin/KLEE_CLEVER'],
    packages     = find_packages(),
    package_dir  = {'CLEVER': 'CLEVER'},
    install_requires=[
        'pycparser>=0.1'
    ]
)

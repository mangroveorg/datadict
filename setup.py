#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

setup(name='datadict',
      version='0.1',
      description='Remote data dictionary providing shareable definition',
      author='Mangroveorg',
      author_email='mangrove@googlegroups.com',
      url='https://github.com/mangroveorg/datadict',
      packages=find_packages('.'),
      install_requires=['CouchDB'],
      license='BSD'
)


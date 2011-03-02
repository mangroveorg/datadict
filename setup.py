#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup
import os
import sys

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if root_dir != '':
    os.chdir(root_dir)
sys.path.insert(0, root_dir)


def fullsplit(path, result=None):
    """
    Split a pathname into components (the opposite of os.path.join) in a
    platform-neutral way.
    """
    if result is None:
        result = []
    head, tail = os.path.split(path)
    if head == '':
        return [tail] + result
    if head == path:
        return result
    return fullsplit(head, [tail] + result)
    
    

def get_packages(datadict_dir):
    """ 
        Compile the list of packages available, because distutils doesn't have
        an easy way to do this.
    """
    packages, data_files = [], []

    for dirpath, dirnames, filenames in os.walk(datadict_dir):
        # Ignore dirnames that start with '.'
        for i, dirname in enumerate(dirnames):
            if dirname.startswith('.'): del dirnames[i]
        if '__init__.py' in filenames:
            packages.append('.'.join(fullsplit(dirpath)))
        elif filenames:
            data_files.append([dirpath, [os.path.join(dirpath, f) for f in filenames if f != 'setup.py']])
            
        return packages, data_files

packages, data_files = get_packages('datadict')

setup(
    name='datadict',
    version = __import__('datadict').__version__,
    packages = packages,
    data_files = data_files,
    description='Remote data dictionary providing shareable definition',
    author='Mangroveorg',
    author_email='mangrove@googlegroups.com',
    url='https://github.com/mangroveorg/datadict',
    install_requires=['CouchDB'],
    license='BSD'
)


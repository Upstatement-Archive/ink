#!/usr/bin/env python
"""
Ink
======

Ink is a set of command-line database and asset managment tools for wordpress
projects. It specializes in archiving + syncing database images, and is meant
to cut down on the messy exchanges that can suffocate rapid wordpress dev.

Tools for Small Wordpress Teams
-------------------------------

At it's core, Ink is just a bunch of deployment scripts. Ink provides these in
a wordpress workflow context, which automates messy database synchronousity.

Right now Ink relies on Fabric, Dropbox, and MySQL. The sample .inkrc is
tailored for MAMP-based MySQL installs. See the README for  more information.

:copyright: (c) 2013 by Upstatement, see AUTHORS for more details.
"""

from setuptools import setup


install_requires = [
    'Fabric==1.6.0',
    'distribute==0.6.31',
    'paramiko==1.10.0',
    'pycrypto==2.6',
    'wsgiref==0.1.2',
]

setup(
    name='ink',
    version='0.2.1a',
    author='Pete Karl II',
    author_email='pete@upstatement.com',
    packages=['ink'],
    package_dir={'ink': 'ink'},
    description='CLI for MySQL database synchronousity.',
    install_requires=install_requires,
    data_files=[('ink', ['ink/ink.py', 'ink/fabfile.py'])]
)

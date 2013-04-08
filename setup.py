#!/usr/bin/env python
"""
Nib
======

Nib is a set of command-line database and asset managment tools for wordpress
projects. It specializes in archiving + syncing database images, and is meant
to cut down on the messy exchanges that can suffocate rapid wordpress dev.

Tools for Small Wordpress Teams
-------------------------------

At it's core, Nib is just a bunch of deployment scripts. Nib provides these in
a wordpress workflow context, which automates messy database synchronousity.

Right now Nib relies on Fabric, Dropbox, and MySQL. The sample .nibrc is
tailored for MAMP-based MySQL installs. See the README for  more information.

:copyright: (c) 2013 by Upstatement, see AUTHORS for more details.
"""

from setuptools import setup


install_requires = [
    'Fabric==1.6.0',
    'MySQL-python==1.2.4',
    'distribute==0.6.31',
    'nib==0.0.1',
    'paramiko==1.10.0',
    'pycrypto==2.6',
    'wsgiref==0.1.2',
]

setup(
    name='nibtools',
    version='0.1.1a',
    author='Pete Karl II',
    author_email='pete@upstatement.com',
    include_package_data=True,
    description='CLI for MySQL database synchronousity.',
    install_requires=install_requires,
    scripts=[
        'src/nib.py'
    ],
    package_data={
        "nibtools": ['src/static/fabfile.py'],
    },
)

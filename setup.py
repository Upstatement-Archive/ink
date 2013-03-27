#!/usr/bin/env python
"""
Nib
===

Nib is a set of tools to assist with Wordpress development across small teams.

:copyright: (c) 2013 by Upstatement, see AUTHORS for more details.
"""

from setuptools import setup, find_packages

setup(
    name='nib',
    version='0.0.1',
    author='Pete Karl II',
    author_email='pete@upstatement.com',
    description='A Wordpress development toolkit',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    zip_safe=False,
    license='BSD',
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: POSIX :: Linux',
        'Topic :: Software Development'
    ],
)

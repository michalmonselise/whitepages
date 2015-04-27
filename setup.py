#!/usr/bin/env python

from setuptools import setup

setup(
    name='whitepages',
    version='0.0.1',
    author='Michal Monselise',
    author_email='michal.monselise@gmail.com',
    packages=['whitepages', 'whitepages.test'],
    # url='https://github.com/michalmonselise/whitepages',
    license='LICENSE.txt',
    description='Python wrapper for White Pages API',
    long_description=open('README.md').read(),
    requires=['unittest2'],
)
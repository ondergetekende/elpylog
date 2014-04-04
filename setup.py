#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='elpylog',
    version='0.1.0',
    description="Python logger sending",
    long_description=open('README.md').read(),

    author='Koert van der Veer',
    author_email='opensource@ondergetekende.nl',

    include_package_data=True,
    keywords='logging elasticsearch bulk udp logstash',
    license='BSD License',
    packages=find_packages(),
    url='git@github.com:ondergetekende/elpylog.git',
    zip_safe=False,
)

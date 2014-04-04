#!/usr/bin/env python

from setuptools import setup

version = '0.1.1'

setup(
    name='elpylog',
    version=version,
    description="Python logger sending it's logs to elasticsearch.",
    keywords='logging elasticsearch bulk udp logstash',
    #long_description=open('README.md').read(),

    author='Koert van der Veer',
    author_email='opensource@ondergetekende.nl',
    download_url='https://github.com/ondergetekende/elpylog/tarball/%s' % version,
    include_package_data=True,
    license='BSD License',
    packages=['elpylog'],
    url='git@github.com:ondergetekende/elpylog.git',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries",
        "Topic :: System :: Logging",
    ],
)

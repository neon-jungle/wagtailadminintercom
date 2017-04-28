#!/usr/bin/env python
"""
Install wagtailadminintercom using setuptools
"""

from setuptools import find_packages, setup

with open('README.rst', 'r') as f:
    readme = f.read()

with open('wagtailadminintercom/_version.py', 'r') as f:
    version = '0.0.0'
    exec(f.read())

setup(
    name='wagtailadminintercom',
    version=version,
    description="Add an Intercom chat widget inside the Wagtail admin",
    long_description=readme,
    author='Tim Heap',
    author_email='tim@takeflight.com.au',
    url='https://github.com/takeflight/wagtailadminintercom',

    install_requires=[
        'wagtail>=1.9',
    ],
    zip_safe=False,
    license='BSD License',

    packages=find_packages(),

    include_package_data=True,
    package_data={},

    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
    ],
)

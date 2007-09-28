#!/usr/bin/env python
import os
from setuptools import setup, find_packages

def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

setup(
    name='restview',
    version='0.0.3',
    author='Marius Gedminas',
    author_email='marius@gedmin.as',
    url='http://mg.pov.lt/restview/',
    download_url='http://cheeseshop.python.org/pypi/restview',
    description='ReStructuredText viewer',
    long_description=read('README.txt'),
    license='GPL',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Documentation',
        'Topic :: Text Processing :: Markup',
    ],

    py_modules=['restviewhttp'],
    install_requires=['docutils'],
    extras_requires={'syntax': ['pygments']},
    zip_safe=False,
    entry_points="""
    [console_scripts]
    restview = restviewhttp:main
    """,
)
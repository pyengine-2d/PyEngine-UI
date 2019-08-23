#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import pyengine_ui

setup(

    name='PyEngine-2D-UI',

    version=pyengine_ui.__version__,

    packages=find_packages(),
    author="LavaPower",
    author_email="lavapower84@gmail.com",
    description="UI for PyEngine-2D",
    long_description_content_type="text/markdown",
    long_description=open('README.md').read(),

    include_package_data=True,

    url='http://github.com/LavaPower/PyEngine',

    # https://pypi.python.org/pypi?%3Aaction=list_classifiers.
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Intended Audience :: Developers",
    ],
    entry_points={
        'console_scripts':[
            'pyengine = pyengine_ui.pyengine_app:launch',
        ],
    },
    install_requires=['PyEngine-2D>=1.6.0', 'PySide2']
)
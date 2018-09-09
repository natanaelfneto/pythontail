#!/usr/bin/env python
from __future__ import print_function
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pythontail",
    version="0.3",
    author="natanaelfneto",
    author_email="natanaelfneto@outlook.com",
    description="Unix tail implementation in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/natanaelfneto/pythontail",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
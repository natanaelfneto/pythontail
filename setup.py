#!/usr/bin/env python
from __future__ import print_function
import re
import setuptools

with open("README.md", "r") as file:
    long_description = file.read()

setuptools.setup(
    name="pythontail",
    version="0.4",
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
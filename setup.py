#!/usr/bin/env python3

# ||Imports||
########################################################################################################################
from setuptools import setup

# ||Variables||
########################################################################################################################
with open("./README.md", "r", encoding = "utf-8") as readme:
    long_description = readme.read()

packages = [
    "logpy",
    "logpy.ansi",
    "logpy.log"
]

# ||Setup||
########################################################################################################################
setup(
    name = "log.py",
    version = "0.0.1",
    author = "Sebastiaan Bij",
    description = "A basic logging library for Python.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/SebastiaanBij/log.py",
    packages = packages,
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Typing :: Typed"
    ],
    python_requires = ">= 3.10"
)

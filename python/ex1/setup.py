#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from os import path, system

__name__ = "ex1"
__version__ = "1.0.0"

# Get the long description from the relevant file
with open(path.join(path.dirname(__file__), "README.md"), encoding="utf-8") as f:
    long_description = f.read()

install_requires = [
    "numpy",
]

dev_requirements = [
    "pytest-runner",
    "pytest",
    "pytest-timeout",
    "pytest-instafail",
    "pytest-cov",
    "mock",
    "coverage",
]

setup(
    name=__name__,
    version=__version__,
    description="Project for standford first assignment",
    author="Cillian O'Brien",
    long_description=long_description,
    author_email="Cillianobrien01@gmail.com",
    packages=find_packages(),
    install_requires=install_requires,
    package_data={"": ["*.yaml", "*.bin", "*.space", "*.ini", "*.md"]},
    extras_require={"dev": dev_requirements},
)

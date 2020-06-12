#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages

with open("requirements/base.txt") as f:
    required = f.read().splitlines()

setup(
    name="mk-network",
    version="0.0.1",
    description="Simple pure python network package",
    author="Matej Kerekrety",
    author_email="matej.kerekrety@gmail.com",
    packages=find_packages(exclude=("tests",)),
    install_requires=required,
)

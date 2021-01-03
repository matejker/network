#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages

with open("requirements/base.txt") as f:
    required = f.read().splitlines()

setup(
    name="mk-network",
    version="0.0.4",
    description="Simple pure Python package for generating, modifying and playing with (even complex) networks.",
    author="Matej Kerekrety",
    author_email="matej.kerekrety@gmail.com",
    packages=find_packages(exclude=("tests",)),
    install_requires=required,
)

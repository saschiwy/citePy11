# -*- coding: utf-8 -*-
import os
import sys
import subprocess

from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

setup(
    name="citePy11",
    version="0.0.1",
    author="Sascha Schiwy",
    author_email="sascha.schiwy@gmail.com",
    description="Create pybind11 bindings out of a CPP Interface Header.",
    long_description=open('Readme.md').read(),
    install_requires=[
       "robotpy-cppheaderparser",
       "pybind11",
   ],
   license='LICENSE',
   packages=['citePy11'],
)

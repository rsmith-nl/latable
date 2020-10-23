# file: setup.py
# vim:fileencoding=utf-8:ft=python
# Installation script for latable
#
# Author: R.F. Smith <rsmith@xs4all.nl>
# Created: 2018-11-06T18:17:47+0100
# Last modified: 2018-11-06T18:19:16+0100

from distutils.core import setup
from latable import __version__

with open("README.rst") as file:
    ld = file.read()

setup(
    name="latable",
    version=__version__,
    license="MIT",
    description="Module to generate LaTeX tables",
    author="Roland Smith",
    author_email="rsmith@xs4all.nl",
    url="https://github.com/rsmith-nl/latable",
    py_modules=["latable"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Other Environment" "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Printing",
    ],
    long_description=ld,
)

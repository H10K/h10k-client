"""
setup.py: Setup file for the H10K Client.

See https://github.com/H10K/h10kcli
"""
import os
from setuptools import find_packages
from setuptools import setup
import sys

sys.path.insert(0, os.path.abspath('lib'))

exec(open('h10kcli/version.py').read())

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    author="League of Crafty Programmers Ltd",
    author_email="info@locp.co.uk",
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    description="H10K Command Line Interface",
    entry_points={
        'console_scripts': ['h10k=h10kcli.__init__:main'],
    },
    install_requires=[
        'PyYAML'
    ],
    license='BSD-3-Clause',
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="h10kcli",
    packages=find_packages(),
    test_suite='nose.collector',
    tests_require=['nose'],
    url="https://github.com/h10k/h10kcli",
    version=__version__,
)

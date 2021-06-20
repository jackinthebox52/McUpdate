from setuptools import setup
import os

setup(
    name='McUpdate',      # name of PyPI package
    version='0.1',          # version number, update with new releases
    package_data={
        # If any package contains *.txt files, include them:
        "": ["*.py"],
        # And include any *.dat files found in the "data" subdirectory
        # of the "mypkg" package, also:
        #"mypkg": ["data/*.dat"],
    }
)

from setuptools import setup
from setuptools.command.install import install
import os

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        os.system("cat testing.egg-info/PKG-INFO")

setup(
    name='McUpdate',      # name of PyPI package
    version='0.1',          # version number, update with new releases
    description='The simplest setup in the world',
      classifiers=[
        'Development Status :: 0.1 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Runtime :: Python :: 3.0',
      ],
    author='jackinthebox52',
    author_email='jackmassey2000@gmail.com',
    license='MIT',
    package_data={
        # If any package contains *.txt files, include them:
        "": ["*.py"],
        # And include any *.dat files found in the "data" subdirectory
        # of the "mypkg" package, also:
        #"mypkg": ["data/*.dat"],
    }
)

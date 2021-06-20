#!/usr/bin/python
import os, stat
from setuptools import setup

setup(
    name='MCUpdate',      # name of PyPI package
    version='0.1',          # version number, update with new releases
    packages=['mcupdate'] # names of packages directories
)

loc = input('Set install location. Default (/usr/local/bin/):')
if(loc == ''):
    loc = '/usr/local/bin/'

st = os.stat('./main.py')
os.chmod('./main.py', st.st_mode | stat.S_IEXEC) #CHMOD +x

os.symlink('./main.py', loc + 'mcupdate')
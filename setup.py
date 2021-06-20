#!/usr/bin/python
from setuptools.command.install import install
import os, subprocess
import PyInstaller

# my spec file in "dev\config" dir
workdir = os.getcwd()
fn_msi_spec = os.path.join(workdir, 'main_msi.spec')

# define the "dev\dist" and "dev\build" dirs
distdir = os.path.join(workdir, 'dist')
builddir = os.path.join(workdir, 'build')

# call pyinstaller directly
subprocess.call("python -m PyInstaller --noconsole --name WorkLogger {0}".format('main.py'), shell = True)
print('[MCUPDATE SETUP]: Binary built from python files')


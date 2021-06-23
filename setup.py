#!/usr/bin/python
from setuptools.command.install import install
import os, subprocess, pwd
import PyInstaller

# Spec file in 'dev\config'
workdir = os.getcwd()
fn_msi_spec = os.path.join(workdir, 'main_msi.spec')

# 'dev\dist' and 'dev\build' dirs
distdir = os.path.join(workdir, 'dist')
builddir = os.path.join(workdir, 'build')

# Call PyInstaller bash subprocess
subprocess.call("python -m PyInstaller --noconsole --name mcupdate {0}".format('main.py'), shell = True)
print('[MCUPDATE SETUP]: Binary built from python files.')

subprocess.call("sudo rm /usr/bin/mcupdate", shell = True)
subprocess.call("sudo rm -r /usr/local/mcupdate", shell = True)
print('[MCUPDATE SETUP]: 2 errors = fine!')

# Create symlink to /usr/bin
subprocess.call("sudo mv {0}/mcupdate /usr/local".format(distdir), shell = True)
subprocess.call("sudo ln -s /usr/local/mcupdate/mcupdate /usr/bin", shell = True)
print('[MCUPDATE SETUP]: Installed dist to /usr/local/mcupdate/')

subprocess.call("sudo mkdir /usr/local/mcupdate/db", shell = True)
print('[MCUPDATE SETUP]: Created database dir at /usr/local/mcupdate/db')

print("[MCUPDATE SETUP]: Setup complete. Run 'mcupdate -h for help.'")

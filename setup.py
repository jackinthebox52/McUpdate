#!/usr/bin/python
from setuptools.command.install import install
import os, subprocess, pwd
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

with open('/home/{0}/.bash_profile'.format(pwd.getpwuid(os.getuid())[0])) as f:
    lines = f.readlines()

    path = ('export mcupdate={0}/main/main'.format(distdir) + '\n')
    skip = False
    for l in lines:
        if l == path:
            skip = True

    if not skip:
        lines.append(path)
        w = ' '.join(lines)
        with open('/home/{0}/.bash_profile'.format(pwd.getpwuid(os.getuid())[0]), "w") as f:
            f.write(w)
        print('[MCUPDATE SETUP]: Modified path at bash_profile. Added mcupdate command.')


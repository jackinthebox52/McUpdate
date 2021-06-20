#!/usr/bin/python
import os, stat

loc = input('Set install location. Default (/usr/local/bin/):')
if(loc == ''):
    loc = '/usr/local/bin/'

st = os.stat('./main.py')
os.chmod('./main.py', st.st_mode | stat.S_IEXEC) #CHMOD +x

os.symlink('./main.py', loc + 'mcupdate')
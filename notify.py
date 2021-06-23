import subprocess

def notifySend(text): #TODO not yet used
    subprocess.call("notify-send --app-name=McUpdate '{0}'".format(text), shell = True)
    print('[MCUPDATE SETUP]: Binary built from python files.')
#!/usr/bin/python
"""
McUpdate is open source, distrubuted under The MIT License
                       https://opensource.org/licenses/MIT

AIO Server Management Tool
With downloads and auto-updates, and simple command line usage

by https://github.com/jackinthebox52
"""
import spigot, paper
import shutil, unicodedata, os, sys, signal, stat , pwd


VERSION = ""
SERVER = ""
WDIR = ""
RMIN = "1G"
RMAX = "1G"

def getUsername():
    return pwd.getpwuid( os.getuid() )[ 0 ]

def parseArgs():
    global VERSION, SERVER, WDIR, RMIN, RMAX
    arglen = len(sys.argv)
    if(arglen >= 2):#Min amount of args
        for a in sys.argv:
            if sys.argv[1] == "install":
                if a.find("=") != -1:
                    sp = a.split("=")
                    if sp[0] == "version":
                        VERSION = sp[1]
                    if sp[0] == "server":
                        if sp[1] == "paper" or sp[1] == "spigot":
                            SERVER = sp[1]
                    if sp[0] == "ram":
                        if sp[1].find(":") != -1:
                            RMIN = sp[1].split(":")[0]
                            RMAX = sp[1].split(":")[1]      
                    if sp[0] == "dir":
                        WDIR = sp[1]

            if sys.argv[1] == "config":
                if a.find("=") != -1:
                    sp = a.split("=")
                    if sp[0] == "version":
                        VERSION = sp[1] #TODO placeholder code, replace.
                        
            
            if a.find("-") != -1:
                    sp = a.split("-")
                    if sp[0] == '' and (sp[1] == 'h' or sp[1] == 'help'):
                        print("[MCUPDATE]: Some help using mcupdate:" + WDIR)
                        print('    Example: mcupdate -h or -help')
                        print('    Example: mcupdate install server=paper version=latest')
                        print('        Specify a minecraft version with version=x.xx.x')
                        print('        Examples: version=1.17.0, version=1.10.5, spigot can use version=latest');print()
                        print('        Specify the server software with server=xxxx')
                        print('        Options: server=paper, server=spigot') ;print()
                        print('        Specify amount of ram with ram=MIN:MAX')
                        print('        Examples: ram=500M:1G, ram=2G:2G'); print()
                        print('        Specify a server install directory with dir=xxxx')
                        print('        Example: dir=/usr/mcserver')
                        sys.exit()
    else:
        print('[FATAL]: Missing args. Use "-h" for help.')
        sys.exit()
    return
            
def run():
    global WDIR
    parseArgs()

    if(WDIR == ""):
        WDIR = "/home/{0}/mcserver/".format(getUsername())
        print("[WARNING]: Using default home directory for install: ~/mcserver. Will overwrite existing directory.")
        input("Press Enter to confirm")
    try:
        os.mkdir(WDIR)
    except:
        print("[MCUPDATE]: Removing directory: " + WDIR)
        shutil.rmtree(WDIR)
        os.mkdir(WDIR)
    os.chdir(WDIR)

    if SERVER == "spigot":
        spigot.downloadSpigot(VERSION, RMIN, RMAX, WDIR)
    if SERVER == "paper":
        paper.downloadPaper(VERSION, RMIN, RMAX, WDIR)
run()
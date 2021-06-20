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
    if(arglen >= 2):
        for a in sys.argv:
            if a.find("=") != -1:
                split1 = a.split("=")
                if split1[0] == "version":
                    VERSION = split1[1]
                if split1[0] == "server":
                    if split1[1] == "paper" or split1[1] == "spigot":
                        SERVER = split1[1]
                if split1[0] == "ram":
                    if split1[1].find(":") != -1:
                        RMIN = split1[1].split(":")[0]
                        RMAX = split1[1].split(":")[1]      
                if split1[0] == "wdir" or split1[0] == "dir" or split1[0] == "workingdir":
                    WDIR = split1[1]
                    
        return
    print('Specify a minecraft version (eg. 1.16.5 || 1.17.0) or use "latest" to get the latest version. Or use "help"')
    return 'err'
            
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
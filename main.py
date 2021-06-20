"""
McUpdate is open source, distrubuted under The MIT License
                       https://opensource.org/licenses/MIT

AIO Server Management Tool
With downloads and auto-updates, and simple command line usage

by https://github.com/jackinthebox52
"""
import shutil, unicodedata, os, subprocess, sys, requests, signal, time, stat

VERSION = ""
SERVER = ""
WDIR = ""
RMIN = "1G"
RMAX = "1G"

def downloadPaper():
    paper = 'https://papermc.io/api/v1/paper/'
    paper = paper + VERSION +  '/latest/download' # Assemble download string
    r = requests.get(paper, allow_redirects=True)
    open(WDIR + 'paper.jar', 'wb').write(r.content) #Make request then write contents to file

    javastr = "java -Xms{0} -Xmx{1} -jar {2}paper.jar --nogui".format(RMIN, RMAX, WDIR)
    open(WDIR + 'start.sh', 'wb').write(str.encode(javastr))
    os.chmod(WDIR + 'start.sh', stat.S_IXGRP) #CHMOD +x all  users

    runPaper()
    print("[MCUPDATE]: Downloaded and configured PaperMC server at " + WDIR)
    print("[MCUPDATE]: Launch start bash in directory:" + WDIR + " with ./start.sh")
    return


def runPaper():
    print('[MCUPDATE]: Running paper jar to setup')

    javastr = "java -Xms{0} -Xmx{1} -jar {2}paper.jar --nogui".format(RMIN, RMAX, WDIR)
    subprocess.run(javastr, shell=True)

    acceptEULA(WDIR)
    print("[MCUPDATE]: Accepted EULA")

    p = subprocess.Popen(javastr, shell = True)
    time.sleep(30)#TODO check stdout and close when server is done
    p.kill() 
    print("[MCUPDATE]: Closed PaperMC server")
    return

def downloadSpigot():
    global WDIR
    path = WDIR
    spigot = 'https://hub.spigotmc.org/jenkins/job/BuildTools/lastBuild/artifact/target/BuildTools.jar'
    r = requests.get(spigot, allow_redirects=True)

    open(path + 'BuildTools.jar', 'wb').write(r.content)
    if(VERSION=="latest"):
        subprocess.call('java -jar ' + path + 'BuildTools.jar', shell=True)
    else:
        subprocess.call('java -jar ' + path + 'BuildTools.jar --rev ' + VERSION, shell=True)
    cleanseFolder(path, "spigot-")
    return

def acceptEULA(path):
    os.rename(path + "eula.txt", path +"eulatmp.txt")
    fin = open(path +"/eulatmp.txt", "rt")
    fout = open(path +"/eula.txt", "wt")
    #for each line in the input file
    for line in fin:
        #read replace the string and write to output file
        fout.write(line.replace('eula=false', 'eula=true'))
    #close input and output files
    fin.close()
    fout.close()
    os.remove(path +"/eulatmp.txt")


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

def cleanseFolder(directory, prefix):
    count = 0
    for item in os.listdir(directory):
        path = os.path.join(directory, item)
        if not item.startswith(prefix):
            if os.path.isfile(path):
                os.remove(path)
                print("[MCUPDATE][{0}]: Deleting build file @ ".format(count) + path)
                count += 1
            elif os.path.isdir(os.path.join(directory, item)):
                shutil.rmtree(path)
                print("[MCUPDATE][{0}]: Deleting multiple build files @ ".format(count) + path)
                count += 1
            else:
                print("A simlink or something called {} was not deleted.".format(item))

            
def run():
    global VERSION, WDIR, SERVER
    parseArgs()

    if(WDIR == ""):
        WDIR = "~/mcserver"
        print("[WARNING]: Using default home directory for install: ~/mcserver. Will overwrite existing directory.")
        input("Press Enter to confirm")
    else:
        try:
            os.mkdir(WDIR)
        except:
            print("[MCUPDATE]: Removing directory:" + WDIR)
            shutil.rmtree(WDIR, ignore_errors=True)
            os.mkdir(WDIR)
        os.chdir(WDIR)

    if SERVER == "spigot":
        downloadSpigot()
    if SERVER == "paper":
        downloadPaper()
run()
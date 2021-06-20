import shutil, unicodedata, os, subprocess, sys, requests, signal, time

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
    return

def downloadSpigot():
    global WDIR
    path = WDIR + "./spigot/"
    try:
        os.mkdir(path)
    except FileExistsError:
        shutil.rmtree(path , ignore_errors=True)
    spigot = 'https://hub.spigotmc.org/jenkins/job/BuildTools/lastBuild/artifact/target/BuildTools.jar'
    r = requests.get(spigot, allow_redirects=True)

    open(path + 'BuildTools.jar', 'wb').write(r.content)
    if(VERSION=="latest"):
        subprocess.call('java -jar ' + path + 'BuildTools.jar', shell=True)
        return
    else:
        subprocess.call('java -jar ' + path + 'BuildTools.jar --rev ' + VERSION, shell=True)
        return
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
            
def run():
    global VERSION, WDIR, SERVER
    parseArgs()

    if(WDIR == ""):
        print("[WARNING]: Using current directory as working directory, this is discouraged.")
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
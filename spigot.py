import subprocess, requests, os, time, shutil, time, stat

def downloadSpigot(VERSION, RMIN, RMAX, WDIR):
    path = WDIR
    spigot = 'https://hub.spigotmc.org/jenkins/job/BuildTools/lastBuild/artifact/target/BuildTools.jar'
    r = requests.get(spigot, allow_redirects=True)

    open(path + 'BuildTools.jar', 'wb').write(r.content)
    if(VERSION=="latest"):
        subprocess.call('java -jar ' + path + 'BuildTools.jar', shell=True)
    else:
        subprocess.call('java -jar ' + path + 'BuildTools.jar --rev ' + VERSION, shell=True)

    print('[MCUPDATE]: Cleansing build tools')
    cleanseFolder(path, 'spigot-', WDIR)

    print('[MCUPDATE]: Creating start.sh, run with ./start.sh')
    javastr = "java -Xms{0} -Xmx{1} -jar {2}spigot-* --nogui".format(RMIN, RMAX, WDIR)
    open(WDIR + 'start.sh', 'wb').write(str.encode(javastr))
    st = os.stat(WDIR + 'start.sh')
    os.chmod(WDIR + 'start.sh', st.st_mode | stat.S_IEXEC) #CHMOD +x

    runSpigot(WDIR)
    
    return


def cleanseFolder(directory, prefix, WDIR):
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
                print("[MCUPDATE][{1}]A simlink or something called {0} was not deleted.".format(item, count))
    return

def runSpigot(WDIR):
    print('[MCUPDATE]: Running Spigot jar to setup')

    javastr = "{0}./start.sh".format(WDIR)
    subprocess.run(javastr, shell=True)

    acceptEULA(WDIR)
    print("[MCUPDATE]: Accepted EULA")

    p = subprocess.Popen(javastr, shell = True)
    time.sleep(45)#TODO check stdout and close when server is done
    p.kill() 
    print("[MCUPDATE]: Closed Spigot server")
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
import os, requests, stat, subprocess, time

def downloadPaper(VERSION, RMIN, RMAX, WDIR):
    paper = 'https://papermc.io/api/v1/paper/'
    paper = paper + VERSION +  '/latest/download' # Assemble download string
    r = requests.get(paper, allow_redirects=True)
    open(WDIR + 'paper.jar', 'wb').write(r.content) #Make request then write contents to file

    javastr = "java -Xms{0} -Xmx{1} -jar {2}paper.jar --nogui".format(RMIN, RMAX, WDIR)
    open(WDIR + 'start.sh', 'wb').write(str.encode(javastr))
    st = os.stat(WDIR + 'start.sh')
    os.chmod(WDIR + 'start.sh', st.st_mode | stat.S_IEXEC) #CHMOD +x

    runPaper(WDIR)
    print("[MCUPDATE]: Downloaded and configured PaperMC server at " + WDIR)
    print("[MCUPDATE]: Launch start bash in directory:" + WDIR + " with ./start.sh")
    return


def runPaper(WDIR):
    print('[MCUPDATE]: Running Paper jar to setup')

    javastr = "{0}./start.sh".format(WDIR)
    subprocess.run(javastr, shell=True)

    acceptEULA(WDIR)
    print("[MCUPDATE]: Accepted EULA")

    p = subprocess.Popen(javastr, shell = True)
    time.sleep(45)#TODO check stdout and close when server is done
    p.kill() 
    print("[MCUPDATE]: Closed PaperMC server")
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
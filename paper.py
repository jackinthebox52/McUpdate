import os, requests, stat, subprocess, time
import main

def downloadPaper():
    paper = 'https://papermc.io/api/v1/paper/'
    paper = paper + main.VERSION +  '/latest/download' # Assemble download string
    r = requests.get(paper, allow_redirects=True)
    open(main.WDIR + 'paper.jar', 'wb').write(r.content) #Make request then write contents to file

    javastr = "java -Xms{0} -Xmx{1} -jar {2}paper.jar --nogui".format(main.RMIN, main.RMAX, main.WDIR)
    open(main.WDIR + 'start.sh', 'wb').write(str.encode(javastr))
    os.chmod(main.WDIR + 'start.sh', stat.S_IXGRP) #CHMOD +x all  users

    runPaper()
    print("[MCUPDATE]: Downloaded and configured PaperMC server at " + main.WDIR)
    print("[MCUPDATE]: Launch start bash in directory:" + main.WDIR + " with ./start.sh")
    return


def runPaper():
    print('[MCUPDATE]: Running paper jar to setup')

    javastr = "java -Xms{0} -Xmx{1} -jar {2}paper.jar --nogui".format(main.RMIN, main.RMAX, main.WDIR)
    subprocess.run(javastr, shell=True)

    main.acceptEULA(main.WDIR)
    print("[MCUPDATE]: Accepted EULA")

    p = subprocess.Popen(javastr, shell = True)
    time.sleep(30)#TODO check stdout and close when server is done
    p.kill() 
    print("[MCUPDATE]: Closed PaperMC server")
    return
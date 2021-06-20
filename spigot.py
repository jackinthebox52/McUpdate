import subprocess, requests, os, time, shutil
import main

def downloadSpigot():
    path = main.WDIR
    spigot = 'https://hub.spigotmc.org/jenkins/job/BuildTools/lastBuild/artifact/target/BuildTools.jar'
    r = requests.get(spigot, allow_redirects=True)

    open(path + 'BuildTools.jar', 'wb').write(r.content)
    if(main.VERSION=="latest"):
        subprocess.call('java -jar ' + path + 'BuildTools.jar', shell=True)
    else:
        subprocess.call('java -jar ' + path + 'BuildTools.jar --rev ' + main.VERSION, shell=True)
    
    print("[MCUPDATE]: Cleansing build tools")
    cleanseFolder(path, "spigot-")
    return

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
                print("[MCUPDATE][{1}]A simlink or something called {0} was not deleted.".format(item, count))
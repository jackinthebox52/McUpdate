# MCUpdate [In Development]

## Simple Minecraft server download and upgrade tool (spigot, papermc, vanilla)

### Requirements
    - Python >= 3.0.0
    - PIP package manager
    - pip -r requirements.txt

### Setup
    1. Change directory to MCUpdate install directory
    2. Command: git clone https://github.com/jackinthebox52/McUpdate.git
    3. Command ./setup.py

### Arguments
    - Using arguments: python main.py version=x.xx.x server=paper

    - * Minecraft Version (eg. version=1.16.5) Must be a valid server number from the server type download page.
    - * Server Type (eg. server=paper, server=spigot)
    - RAM To Allocate To The Server, Min and Max (eg. ram=1028M:2056M, ram=1G:2G). Defaults to 1G:1G
    - Install Directory (eg dir=/home/{user}/newserver/, wdir=/home/{user}/mcserver/) Defaults to ~/mcserver

    [ * = Required ]
    
### Examples
    Bash: python main.py server=paper version=1.16.5 dir=/home/{user}/testsrv/ ram=1G:1G
          python main.py server=spigot version=latest dir=./mcserver/ ram=2G:4G

### INFO
    This software was written and tested on arch linux, it may not work on windows.
    MCUpdate should work on most posix operating systems that have Python 3 installed.

    MCUpdate is open source, distrubuted under The MIT License.
                            https://opensource.org/licenses/MIT

    


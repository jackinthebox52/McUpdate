# MCUPDATE

## Minecraft server download and upgrade tool

### Setup
    1. Change directories to McUpdate install directory
    2. Command: git clone https://github.com/jackinthebox52/McUpdate.git

### Arguments
    - Using arguments: python main.py version=x.xx.x server=paper

    - Minecraft Version (eg. version=1.16.5) *
    - Server Type (eg. server=paper, server=spigot) *
    - RAM To Allocate To The Server, Min and Max (eg. ram=1028M:2056M, ram=1G:2G). Defaults to 1G:1G
    - Install Directory (eg dir=~/newserver/, wdir=/home/{user}/mcserver/) Defaults to current directory (Not recommended)

    [ * = Required ]
    
### Examples
    Bash: python main.py server=paper version=1.16.5 dir=/home/jack/testsrv/ ram=1G:1G

    (written and tested on arch linux)
    


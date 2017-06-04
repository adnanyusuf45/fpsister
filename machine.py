from __future__ import print_function
from os import listdir
from os.path import isfile, join
import os
import socket
import shutil
import sys
import Pyro4
from Pyro4.util import SerializerBase

state = "Folder1/"
host = "10.151.43.75"
port_pyro= 9091
pyroname="machine2"
server = Pyro4.core.Proxy("PYRO:example.dc.dispatcher@10.151.43.75:9096")

@Pyro4.expose
class Machine(object):

    def __init__(self):

        val=self.pyro()
        print(val)
        server.getPyroname(val)

    def touch(self,file):
        open(state+file,'a').close()

    def save(self, file, name):
        copied_file = open(state+name,'a')
	    copied_file.write(file)
	    copied_file.close()

    def rm(self,file):
        os.remove(state+file)

    def getList(self):
        onlyfiles = [f for f in listdir(state) if isfile(join(state,f)) ]
        return onlyfiles

    def getState():
        print(state)

    def setState(path):
        state=path

    def getData(self,path):
        file = open(state+path,'r')
        sentfile = file.read()
        return sentfile

    def pyro(self):
        val = ({"machine":pyroname+"@"+host+":"+str(port_pyro),"path":state})
        return val

if __name__ == "__main__":
    Pyro4.config.HOST = host
    Pyro4.Daemon.serveSimple(
        {
            Machine(): pyroname
        }, verbose=True, ns=False, port=port_pyro
    )

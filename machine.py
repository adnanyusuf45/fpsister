from __future__ import print_function
from os import listdir
from os.path import isfile, join
import os
import socket
import shutil
import sys
import Pyro4
from Pyro4.util import SerializerBase

state = "E:/"
host = "10.151.44.138"
port= "8080"
pyroname="machine1"
server = Pyro4.core.Proxy("PYRONAME:server@10.151.44.110:60345")

@Pyro4.expose
class Machine(object):


    #def main():
        #getState()
    #    server = Pyro4.core.Proxy("PYRONAME:server")
    #    WORKERNAME = "Worker_%d@%s" % (os.getpid(), socket.gethostname())
    #    print(WORKERNAME)
        #state = "E:/"
        #file="E:/test.txt"
        #touch(state,file)
        #cp(file,"F:/")
        #rm(state,file)
        #ls("F:/")
        #index=10
        ##word=[{'machine':'arya','path':'arya'},{'machine':'rijal','path':'rijal'}]
        ##word.append({'machine':'arya','path':'arya'})
        #print word[2]['machine']
        #print(getData("E:/logs.txt"))
        #file = open("E:/its.py",'w')
        #for item in getData("E:/test.py"):
        #    file.write(item)
        #file.close
        #file=getData("E:/logs.txt")
        #file2=open("log.txt",'w')
        #file2=file
        #file2.close()
        #file.close()
        #file.write(getData("E:/logs.txt"))

    def __init__(self):
        print(self.getPyroname())

    def touch(file):
        open(state+file,'a').close()

    def rm(file):
        os.remove(file)

    def getList(state):
        #mypath = "E:/"
        #ls = []
        onlyfiles = [f for f in listdir(state) if isfile(join(state,f)) ]
        return onlyfiles
        #for item in onlyfiles:
            #print(item)

    def getState():
        print(state)

    def setState(path):
        state=path

    def getData(path):
        file = open(path,'r')
        sentfile = file.read()
        return sentfile

    def getPyroname(self):
        #server.setUri(pyroname+"@"+host+":"+port)
        return pyroname+"@"+host+":"+port

if __name__ == "__main__":
    Pyro4.config.HOST = host
    #Pyro4.config.SERVERTYPE = "thread"
    Pyro4.Daemon.serveSimple(
        {
            Machine(): pyroname
        }, verbose=True, ns=False
    )
    #getPyroname()

    #main()

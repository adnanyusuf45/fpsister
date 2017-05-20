__author__ = 'AryaBawanta'
from os import listdir
from os.path import isfile, join
import os
import shutil

state = "E:/"

def main():
    getState()
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

if __name__ == "__main__":
    main()

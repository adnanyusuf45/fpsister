from __future__ import print_function, division
import zipfile
import time
from collections import Counter
import Pyro4
import sys

dispatcher = Pyro4.core.Proxy("PYRO:example.dc.dispatcher@10.151.62.36:9096")

def sendcommand(result):
        if (result[0] == "mv"):
            if(len(result)== 3):
                print ("testA \n")
                src = result[1]
                dst = result[2]
                main()
            else:
                print("wrong command \n")
                print("the correct command is mv /source /destination \n")
                main()
        elif (result[0] == "ls"):
            #print ("testB")
            #print("Content List: \n")
            for item in dispatcher.listFile():
                print(item)
            ##print(server.getFolder())
            main()
        elif (result[0] == "rm"):
            if(len(result)== 2):
                print ("testC \n")
                direc = result[1]
                main()
            else:
                print("wrong command \n")
                print("the correct command is rm filename \n")
                main()
        elif (result[0] == "cp"):
            if(len(result)== 3):
                print ("testD \n")
                src = result[1]
                dst = result[2]
                main()
            else:
                print("wrong command \n")
                print("the correct command is cp /source /destination \n")
                main()
        elif (result[0] == "cd"):
            if(len(result)== 2):
                #print ("testE \n")
                direc = result[1]
                if dispatcher.changeDir(direc)==False:
                    print("path salah")
                main()
            else:
                print("wrong command \n")
                print("the correct command is cd /directory \n")
                main()
        elif (result[0] == "touch"):
            if(len(result)== 2):
                print ("testF \n")
                direc = result[1]
                main()
            else:
                print("wrong command \n")
                print("the correct command is touch /file  \n")
                main()
        else:
            print ("Pilihan Salah")
            main()

def main():
	#print("=====================================================")
	#print("Welcome to 2Global Filesystem")
	#print("--Command List--")
	#print("mv /source /destination")
	#print("rm filename")
	#print("cp /source /destination")
	#print("cd /directory")
	#print("touch /file")
	#print("--End Command List--")
	perintah = input(dispatcher.getPath()+"> ")
	result = perintah.split(" ")
	sendcommand(result)
	#with Pyro4.core.Proxy(PYRO) as dispatcher:
		#    dispatcher.load() __name__ == "__main__":
	main()

if __name__ == "__main__":
    main()
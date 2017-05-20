import sys
import Pyro4

def sendcommand(result):
        if (result[0] == "mv"):
            print ("testA")
        elif (result[0] == "ls"):
            print ("testB")
        elif (result[0] == "rm"):
            print ("testC")
        elif (result[0] == "cp"):
            print ("testD")
        elif (result[0] == "cd"):
            print ("testE")
        elif (result[0] == "touch"):
            print ("testF")



def main():
	print("Welcome to 2Global Filesystem")
	print("--Command List--")
	print("mv /source /destination")
	print("rm filename")
	print("cp /source /destination")
	print("cd /directory")
	print("touch /file")
	perintah = input("Enter your command:")
	result = perintah.split(" ")
	sendcommand(result)
	#with Pyro4.core.Proxy(PYRO) as dispatcher:
        #    dispatcher.load()
        
if __name__ == "__main__":
    main()

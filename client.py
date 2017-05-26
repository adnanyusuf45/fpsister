import sys

import Pyro4




def sendcommand(result):
        
	if (result[0] == "mv"):
            
		print ("testA")
			
		if (len(result)==3):				
			print (len(result))
			
		else:
				
			print ("Wrong command!")
				
			print ("The correct command is : mv /source / destination")
        
	elif (result[0] == "ls"):
            
		print ("testB")
			
		if (len(result)==2):
				
			print (len(result))
			
		else:
				
			print ("Wrong command!")
				
			print ("The correct command is : ls")			
        
	elif (result[0] == "rm"):
            
		print ("testC")
			
		if (len(result)==2):
				
			print (len(result))
			
		else:
				
			print ("Wrong command!")
				
			print ("The correct command is : rm filename")
        
	elif (result[0] == "cp"):
            
		print ("testD")
			
		if (len(result)==3):
				
			print (len(result))
			
		else:
				
			print ("Wrong command!")
				
			print ("The correct command is : cp /source /destination")
        
	elif (result[0] == "cd"):
            
		print ("testE")
			
		if (len(result)==2):
				
			print (len(result))
			
		else:
				
			print ("Wrong command!")
				
			print ("The correct command is : cd /directory")
        
	elif (result[0] == "touch"):
            
		print ("testF")
			
		if (len(result)==2):
				
			print (len(result))
			
		else:
				
			print ("Wrong command!")
				
			print ("The correct command is : touch /file")
		
	else:
			
		print ("Command tidak terdaftar")
			
		perintah = input("Enter your command: ")



def main():
	
	print("=====================================================")
	print("Welcome to 2Global Filesystem")
	
	print("--Command List--")
	
	print("mv /source /destination")
	
	print("rm filename")
	
	print("cp /source /destination")
	
	print("cd /directory")
	
	print("touch /file")

	print("--End Command List--")	
	perintah = input("Enter your command:")
	
	result = perintah.split(" ")
	
	sendcommand(result)
	

	#with Pyro4.core.Proxy(PYRO) as dispatcher:
        
		#    dispatcher.load()
        


if __name__ == "__main__":
    
	main()
	
	

	#with Pyro4.core.Proxy(PYRO) as dispatcher:
	
	#	dispatcher.load()
	
	#	sendcommand(command, dispatcher)


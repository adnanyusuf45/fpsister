import sys
import Pyro4

path = ".."
machine = ""
listFile = []
listMachine = []

@Pyro4.expose
class Dispatcher(object):
	
	def setFolder(newFolder):
		listFolder.append(newFolder)
		
	def getFolder(self):
            ls=[]
            global path
            global listMachine
            global listFile
            counter=0
            if path=="..":
                #list=listMachine
                for item in listMachine:
                    temp = item['machine'].split('@')
                    ls.append(temp[0])
            else:
                ls=listFile

            return ls
        	#counters = [Pyro4.Proxy(uri) for uri in all_counters]

	def getPyroname(self,name):
		listMachine.append(name)
		print(name['machine'])
	
	def getMachine(name):
		for i in len(listMachine):
			if val[i]['path'] == name:
				return	val[i]['machine']
			else:
				return "error"
	def getPath(self):
		global path
		return path
		
	def listFile(self):
		#path = listMachine['machine']
		#worker = Pyro4.core.proxy()
		#worker.ls(path);
		global path
		if(path == ".."):
			return self.getFolder()
		else:
			return machine.getFile()
			
	def removeFile(path):
		worker = Pyro4.core.proxy()
		worker.rm(path)
		
	def copyFile(source, dest):
		#worker_pyro = 
		worker = Pyro4.core.proxy()
		worker.cp(source,dest)
		
	def moveFile(source,dest):
		worker = Pyro4.core.proxy()
		worker.mv(source,dest)
		
	def changeDir(self,newPath):
		global path
		global machine
		global listFile
		if (newPath==".."):
		    path=".."
		    return path
		bool=False
		if path=="..":
		    for item in listMachine:
		        temp=item['machine'].split('@')
		        if (temp[0]==newPath):
		            bool=True
		            machine=Pyro4.core.Proxy("PYRO:"+item['machine'])
		            listFile=machine.getList(item['path'])
		            break
		if bool:
		    path+="/"+newPath
		    return path
		else:
		    return False


	def touchFile(path):
		#dirc = getPath()
		#worker = Pyro4.core.proxy(getPyronname()
		#if(dirc==".."):
		#	worker.touchFile
		#else:
		#	touchFile
		worker = Pyro4.core.proxy()
		worker.touch(path)
	
	
if __name__ == "__main__":
	print("Spinning up  dispatcher.")
	Pyro4.config.HOST = '10.151.62.36'
	Pyro4.config.SERVERTYPE = "thread"
	Pyro4.Daemon.serveSimple(
		{
			Dispatcher:    "example.dc.dispatcher"
		}, verbose=True, ns=False, port=9096
	)

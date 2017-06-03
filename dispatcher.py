import sys
import Pyro4

path = ".."
listFolder = []

listMachine = []

@Pyro4.expose
class Dispatcher(object):
	
	def setFolder(newFolder):
		listFolder.append(newFolder)
		
	def getFolder(self):
            ls=[]
            counter=0
            for item in listMachine:
                temp = item['machine'].split('@')
                ls.append(temp[0])
            return ls
        	#counters = [Pyro4.Proxy(uri) for uri in all_counters]

	def getPyroname(gaTauApa,name):
		listMachine.append(name)
		print(listMachine[0]['machine'])		
	
	def getMachine(name):
		for i in len(listMachine):
			if val[i]['path'] == name:
				return	val[i]['machine']
			else:
				return "error"
	def getPath():
		path = listMachine['machine']
		return path;
		
	def setPath(newPath):
		path = newPath;
		
	def listFile(pat):
		#path = listMachine['machine']
		#worker = Pyro4.core.proxy()
		#worker.ls(path);
		if(path == ".."):
			return self.getFolder()
		else:
			return worker.getFile()
			
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
		
	def changeDir(newPath):
		self.setPath(newPath)

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

import sys
import Pyro4

path = "..";
listFolder = []

all_counters = ['PYRO:example.dc.wordcount.1@10.151.37.126:53349',
'PYRO:example.dc.wordcount.2@10.151.37.126:53349',
'PYRO:example.dc.wordcount.3@10.151.37.126:53349',
'PYRO:example.dc.wordcount.4@10.151.37.126:53349',
'PYRO:example.dc.wordcount.5@10.151.37.126:53349']

class Dispatcher(object):

	def setFolder(newFolder)
		listFolder.append(newFolder)
		
	def getFolder(path):
        counters = [Pyro4.Proxy(uri) for uri in all_counters]
        for c in counters:
            c._pyroAsync()   # set proxy in async mode
        roundrobin_counters = cycle(counters)
		
		for chunk in counters:
			counter = next(roundrobin_counters)
			result = counter.ls(path)
			listFolder.append(result)
		
		return listFolder
		
		for proxy in counters:
            proxy._pyroRelease()
		
	def getPath():
		return path;
		
	def setPath(newPath):
		path = newPath;
		
	def listFile(path):
		worker = Pyro4.core.proxy()
		#worker.ls(path);
		if(path == "..")
			return self.getFolder()
		else
			return worker.getFile();
			
	def removeFile(path):
		worker = Pyro4.core.proxy()
		worker.rm(path)
		
	def copyFile(source, dest):
		worker = Pyro4.core.proxy()
		worker.cp(source,dest)
		
	def moveFile(source,dest):
		worker = Pyro4.core.proxy()
		worker.mv(source,dest)
		
	def changeDir(path):
	
	def touchFile(path):
		worker = Pyro4.core.proxy()
		worker.touch(path)
	
	
if __name__ == "__main__":
print("Spinning up  dispatcher.")
Pyro4.config.HOST = '10.151.37.126'
Pyro4.config.SERVERTYPE = "thread"
Pyro4.Daemon.serveSimple(
	{
		Dispatcher:    "example.dc.dispatcher"
	}, verbose=True, ns=False
)
import sys
import Pyro4

path = ".."
#machine = ""
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
                for item in listMachine:
                    temp = item['machine'].split('@')
                    ls.append(temp[0])
            else:
                ls=listFile

            return ls

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
		#global path
		if(path == ".."):
			return self.getFolder()
		else:
			for item in listMachine:
				temp=item['machine'].split('@')
				path_folder = path.split("/")
				if (temp[0]==path_folder[len(path_folder)-1]):
					bool=True
					machine=Pyro4.core.Proxy("PYRO:"+item['machine'])
					return machine.getList()
			
	def removeFile(self, file_path):
		if(path == ".."):
			file_split = file_path.split("/")
			print(len(file_split))
			if(len(file_split)>1):
				for item in listMachine: 
					temp = item['machine'].split('@')
					if(temp[0]==file_split[0]):
						machine=Pyro4.core.Proxy("PYRO:"+item['machine'])
						machine.rm(file_split[1])
						return file_split[1] + " berhasil dihapus"
			else: 									
				return "Can't remove in this folder"
		else:
			for item in listMachine:
				temp=item['machine'].split('@')
				path_folder = path.split("/")
				if (temp[0]==path_folder[len(path_folder)-1]):
				    bool=True
				    machine=Pyro4.core.Proxy("PYRO:"+item['machine'])
				    machine.rm(file_path)
				    return file_path + " berhasil dihapus"

	def sendData(self,sentdata, dest):
		file_split = dest.split("/")
		#print(file_split[1])
		if(len(file_split)>2):
			for item in listMachine:
				temp = item['machine'].split('@')
				if(temp[0]==file_split[1]):
					machine=Pyro4.core.Proxy("PYRO:"+item['machine'])
					machine.save(sentdata,file_split[2])
		elif(len(file_split)>1):
			for item in listMachine:
				temp = item['machine'].split('@')
				if(temp[0]==file_split[0]):
					machine=Pyro4.core.Proxy("PYRO:"+item['machine'])
					machine.save(sentdata,file_split[1])
		else:
 		    print('lalalayeyeyeye')
 		    for item in listMachine:
 		        temp = item['machine'].split('@')
 		        path_folder = path.split("/")
 		        if(temp[0]==path_folder[1]):
 		            machine=Pyro4.core.Proxy("PYRO:"+item['machine'])
 		            machine.save(sentdata,dest)
					#return true
		#else:
			#return false
			

	def copyFile(self,source, dest):
		if (source==dest):
			dst = dest.split(".")
			dest = dst[0] + "_copy."+dst[1]

		if(path == ".."):
			file_split = source.split("/")
			print(len(file_split))
			if(len(file_split)>1):
				for item in listMachine: 
					temp = item['machine'].split('@')
					if(temp[0]==file_split[0]):
						machine=Pyro4.core.Proxy("PYRO:"+item['machine'])
						sentdata = machine.getData(file_split[1])
						self.sendData(sentdata, dest)
						#return file_split[1] + " berhasil dihapus"
			else: 									
				return "Can't copy"
		else:
			for item in listMachine:
				temp=item['machine'].split('@')
				path_folder = path.split("/")
				if (temp[0]==path_folder[len(path_folder)-1]):
				    machine=Pyro4.core.Proxy("PYRO:"+item['machine'])
					#source_new = source.split("/")
				    print(dest)
				    #source_new = source.split("/")
				    source_new = source
				    sentdata = machine.getData(source)
				    self.sendData(sentdata, dest)
					

	def moveFile(self,source,dest):
		if(path == ".."):
			file_split = source.split("/")
			print(len(file_split))
			if(len(file_split)>1):
				for item in listMachine: 
					temp = item['machine'].split('@')
					if(temp[0]==file_split[0]):
						machine=Pyro4.core.Proxy("PYRO:"+item['machine'])
						sentdata = machine.getData(file_split[1])
						machine.rm(file_split[1])
						self.sendData(sentdata, dest)
			else: 									
				return "Can't copy"
		else:
			for item in listMachine:
				temp=item['machine'].split('@')
				path_folder = path.split("/")
				if (temp[0]==path_folder[len(path_folder)-1]):
				    print(item['machine'])
				    machine=Pyro4.core.Proxy("PYRO:"+item['machine'])
				    #source_new = source.split("/")
				    source_new = source
				    print(source_new)
				    sentdata = machine.getData(source_new)
				    machine.rm(source_new)
				    self.sendData(sentdata, dest)
		
	def changeDir(self,newPath):
		global path
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
		            break
		if bool:
		    path+="/"+newPath
		    return path
		else:
		    return False


	def touchFile(self, file_path):
		if(path == ".."):
			file_split = file_path.split("/")
			print(len(file_split))
			if(len(file_split)>1):
				for item in listMachine: 
					temp = item['machine'].split('@')
					if(temp[0]==file_split[0]):
						machine=Pyro4.core.Proxy("PYRO:"+item['machine'])
						machine.touch(file_split[1])
						return file_split[1] + " berhasil dibuat"
			else: 									
				return "Can't touch in this folder"
		else:
			for item in listMachine:
				temp=item['machine'].split('@')
				path_folder = path.split("/")
				if (temp[0]==path_folder[len(path_folder)-1]):
				    machine=Pyro4.core.Proxy("PYRO:"+item['machine'])
				    machine.touch(file_path)
				    return file_path + " berhasil dibuat"
	
	
if __name__ == "__main__":
	print("Spinning up  dispatcher.")
	Pyro4.config.HOST = '10.151.36.156'
	Pyro4.config.SERVERTYPE = "thread"
	Pyro4.Daemon.serveSimple(
		{
			Dispatcher:    "example.dc.dispatcher"
		}, verbose=True, ns=False, port=9096
	)

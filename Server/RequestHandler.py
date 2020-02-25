import os
import json
import shutil
from zipfile import ZipFile

class RequestHandler:
    def __init__(self, clientHandler):
        self.clientHandler = clientHandler

        self.clientSocket = clientHandler.clientSocket
        self.clientAddress = clientHandler.clientAddress

        self.server = clientHandler.server
        self.files = []

    def sort_request(self, request):
        """Sort the appropriate answer by the request
        
        Arguments:
            request {str} -- Request string from the client
        """
        if request.find("GETDIRECTORY") != -1:
            request = request.replace('GETDIRECTORY', "")
            self.send_directory(request)

        if request.find("GETFILE") != -1:
            request = request.replace("GETFILE", "")
            self.send_file(request)

        if request.find("GETFOLDER") != -1:
            request = request.replace("GETFOLDER", "")
            self.send_folder(request)

        if request.find("CREATEFOLDER") != -1:
            request = request.replace("CREATEFOLDER", "")
            self.create_folder(request)

        if request.find("DELETEFOLDER") != -1:
            request = request.replace("DELETEFOLDER", "")
            self.delete_folder(request)

        if request.find("DELETEFILE") != -1:
            request = request.replace("DELETEFILE", "")
            self.delete_file(request)

        if request.find("UPLOADFILE") != -1:
            request = request.replace("UPLOADFILE", "")
            self.get_file(request)
            
        else:
            pass

    def get_file(self, path):
        try:
            self.server.write_log(f"{self.clientAddress} Uploading file to {path}")
        except:
            pass

        self.clientSocket.settimeout(4)
        decode = ""
        with open(path, 'wb') as file:
            while True:
                try:
                    data = self.clientSocket.recv(1024)
                except:
                    break
                try:
                    decode = data.decode(errors="replace")
                except:
                    pass
                if decode.find("FINISHEDHOST+") != -1:
                    file.write(data[:-13])
                    break
                file.write(data)

        self.server.write_log(f"{self.clientAddress} Successfully got the file")
        file.close() 
        self.clientSocket.settimeout(None)  

        self.clientSocket.send("DONE".encode())     

    def send_directory(self, directory):
        """Send all the files details in a given directory
        
        Arguments:
            directory {str} -- The given directory from the client
        """
        files_raw = os.listdir(directory)
        directories = []
        files = []
        for x in range(len(files_raw)):
            filePath = directory + files_raw[x]
            fileSize = os.path.getsize(filePath)
            fileExtension = os.path.splitext(filePath)[1]
            fileExtension = fileExtension [1:]

            if fileExtension == '':
                fileExtension = "folder"
                directories.append((files_raw[x],fileSize , filePath, fileExtension))

            else:
                files.append((files_raw[x],fileSize , filePath, fileExtension))
        
        for x in files:
            directories.append(x)
        
        self.clientSocket.send(json.dumps(directories).encode())

    def send_file(self, filePath):

        self.clientSocket.send(str(os.path.getsize(filePath)).encode())
        self.clientSocket.recv(20)
        self.server.write_log(f"{self.clientAddress} Sending file " + filePath)
        try:
            file = open(filePath, 'rb')
            
            l = file.read(1024)
            while(l):
                self.clientSocket.send(l)
                l = file.read(1024)

            file.close()
            self.clientSocket.send("FINISHEDHOST+".encode())
            self.server.write_log(f"{self.clientAddress} File {filePath} was sended succesfully")
        except:
            self.server.write_log(f"{self.clientAddress} Unexpected error while sending file (Maybe client disconnected?)" + filePath)

    def send_folder(self, folderPath):
        zipFile = ZipFile("temp.zip", 'w')
        files = os.listdir(folderPath)

        for x in files:
            zipFile.write(folderPath + "/" + x)

        zipFile.close()

        self.clientSocket.send(str(os.path.getsize("temp.zip")).encode())

        self.server.write_log(f"{self.clientAddress} Sending zip file of folder {folderPath}")

        try:
            file = open("temp.zip", 'rb')
            
            l = file.read(1024)
            while(l):
                self.clientSocket.send(l)
                l = file.read(1024)

            file.close()
            os.remove("temp.zip")
            self.clientSocket.send("FINISHEDHOST+".encode())
            self.server.write_log(f"{self.clientAddress} Successfully sended zip file of folder {folderPath}")
        except:
            self.server.write_log(f"{self.clientAddress} Unexpected error while sending zip file (Maybe client disconnected?) {folderPath}")

        

    def create_folder(self, name):
        path = self.clientSocket.recv(260).decode()

        try:
            os.mkdir(path + name)
            self.clientSocket.send("SUCCESS".encode())
        except:
            self.clientSocket.send("FAILED".encode())
            self.server.write_log(f"{self.clientAddress} Error deleting a folder in {path} with the name {name}")
            return

        self.server.write_log(f"{self.clientAddress} Created a folder in {path} with the name {name}")  

    def delete_folder(self, path):

        try:
            shutil.rmtree(path)
            self.clientSocket.send("SUCCESS".encode())
            self.server.write_log(f"{self.clientAddress} Deleted the folder {path}")
        except:
            self.clientSocket.send("FAILED".encode())
            self.server.write_log(f"{self.clientAddress} Error deleting a folder at {path}")

    def delete_file(self, path):

        try:
            os.remove(path)
            self.clientSocket.send("SUCCESS".encode())
            self.server.write_log(f"{self.clientAddress} Deleted the file {path}")
        except:
            self.clientSocket.send("FAILED".encode())
            self.server.write_log(f"{self.clientAddress} Error deleting file {path}")
        
    
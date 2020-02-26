import os
import json
import shutil
from zipfile import ZipFile

class RequestHandler:
    def __init__(self, clientHandler):
        """!
        Constructor of the request handler

        @param clientHandler clientHandler: The clientHandler class
        """
        self.clientHandler = clientHandler

        self.clientSocket = clientHandler.clientSocket
        self.clientAddress = clientHandler.clientAddress

        self.server = clientHandler.server
        self.files = []

    def sort_request(self, request):
        """!
        Act accordingly of the comming request

        @param request str: The client request
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
        """!
        Get the given file from the client and store it in the given path

        @param path str: The path for file storage
        """
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
        """!
        Send a list of all the files in a given directory

        @param directory str: The direcotry path for transfer
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
        """!
        Send the client the file he requested

        @param filePath str: The path of the file the client requested
        """
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
        """!
        Send the client the folder he requested

        @param folderPath str: The path of the requested folder
        """
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
        """!
        Create a folder with the given name

        @param name str: The folder name
        """
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
        """!
        Delete the requested folder

        @param path str: The path of the folder to delete
        """
        try:
            shutil.rmtree(path)
            self.clientSocket.send("SUCCESS".encode())
            self.server.write_log(f"{self.clientAddress} Deleted the folder {path}")
        except:
            self.clientSocket.send("FAILED".encode())
            self.server.write_log(f"{self.clientAddress} Error deleting a folder at {path}")

    def delete_file(self, path):
        """!
        Delete the requested file

        @param path str: The path of the file to delete
        """
        try:
            os.remove(path)
            self.clientSocket.send("SUCCESS".encode())
            self.server.write_log(f"{self.clientAddress} Deleted the file {path}")
        except:
            self.clientSocket.send("FAILED".encode())
            self.server.write_log(f"{self.clientAddress} Error deleting file {path}")
        
    
import os
import json

class RequestHandler:
    def __init__(self, clientHandler):
        self.clientHandler = clientHandler
        self.clientSocket = clientHandler.clientSocket
        self.files = []

    def sort_request(self, request):
        """Sort the appropriate answer by the request
        
        Arguments:
            request {str} -- Request string from the client
        """
        if request.find("GETDIRECTORY") != -1:
            request = request.replace('GETDIRECTORY', "")
            self.send_directory(request)

        else:
            pass

    def send_directory(self, directory):
        """Send all the files details in a given directory
        
        Arguments:
            directory {str} -- The given directory from the client
        """
        rootFolder = "Files" + directory

        files_raw = os.listdir(rootFolder)
        directories = []
        files = []
        for x in range(len(files_raw)):
            filePath = "Files" + directory + "/" + files_raw[x]
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

        



        
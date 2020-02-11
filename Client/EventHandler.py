import json
from FileController import *

class EventHandler:
    def __init__(self, client):
        self.client = client
        self.ui = client.ui
        self.index = 0
        
        self.filePackageArray = [FilePackage(self.ui.editButton1, self.ui.deleteButton1, self.ui.downloadButton1, self.ui.filePic1, self.ui.fileName1, self.ui.line1, self),
                                FilePackage(self.ui.editButton2, self.ui.deleteButton2, self.ui.downloadButton2, self.ui.filePic2, self.ui.fileName2, self.ui.line2, self),
                                FilePackage(self.ui.editButton3, self.ui.deleteButton3, self.ui.downloadButton3, self.ui.filePic3, self.ui.fileName3, self.ui.line3, self),
                                FilePackage(self.ui.editButton4, self.ui.deleteButton4, self.ui.downloadButton4, self.ui.filePic4, self.ui.fileName4, self.ui.line4, self),
                                FilePackage(self.ui.editButton5, self.ui.deleteButton5, self.ui.downloadButton5, self.ui.filePic5, self.ui.fileName5, self.ui.line5, self),
                                FilePackage(self.ui.editButton6, self.ui.deleteButton6, self.ui.downloadButton6, self.ui.filePic6, self.ui.fileName6, self.ui.line6, self),
                                FilePackage(self.ui.editButton7, self.ui.deleteButton7, self.ui.downloadButton7, self.ui.filePic7, self.ui.fileName7, self.ui.line7, self)]
        
    def get_socket(self, socket):
        self.clientSocket = socket

    def register_events_handlers(self):
        self.ui.nextButton.clicked.connect(self.connect_wrapper)

    def connect_wrapper(self):
        """
        Wrapper for the connect function for disabling lineEdit accordingly
        """

        self.ui.lineEditPassword.setEnabled(False)
        self.ui.lineEditIP.setEnabled(False)

        self.client.connect()

        self.ui.lineEditPassword.setEnabled(True)
        self.ui.lineEditIP.setEnabled(True)

    def request_files(self, directory):         
        """Send the server request for files details in a specific directory
        
        Arguments:
            directory {str} -- path of wanted files
        
        Raises:
            Exception: Server didn't answer for the files request
        """   
        for x in self.filePackageArray:
            x.remove_file()

        self.clientSocket.send(("GETDIRECTORY" + directory).encode())
        
        try:
            self.files = json.loads(self.clientSocket.recv(1024).decode())
            print(self.files)
        except:
            raise Exception("EventHandler", "Couldnt get file list")
        
        for x in range(len(self.files)):
            self.files[x] = File(self.files[x])
            try:
                self.filePackageArray[x].set_file(self.files[x])
            except:
                break

        for x in self.filePackageArray:
            print(x.file)

        self.update_ui_files()

    def update_ui_files(self):
        for x in range(7):
            self.filePackageArray[x].visibility(True)
        
        for x in self.filePackageArray:
            if x.file == None:
                x.visibility(False)


    def upload_file(filename):
        try:
            file = open(filename, "rb")
        except:
            client_socket.send("FAILED".encode())
            ui.files_text_edit_console.append("\nFile not found")
            return
        
        client.client_socket.send(str(os.path.getsize(filename)).encode())

        print(os.path.getsize(filename))

        client.client_socket.recv(10)

        try:
            print(client.client_socket.sendfile(file, 0))
        except:
            raise Exception("failed uploading file to server")

        file.close()

        ui.files_text_edit_console.append("\nFile uploaded succesfully")

    def download_file(filename):
        reaction = client.client_socket.recv(255).decode()

        if reaction == "FILE NOT FOUND":
            ui.files_text_edit_console.append("FILE NOT FOUND")
            return     

        filename = "Files/" + filename

        file_size = int(client.client_socket.recv(100))       # Get file size from server
        client.client_socket.send("READY FOR FILE".encode())  # Report the server we are ready for file transfer
        start_time = time.time()                            # Start counting down download time

        file = open(filename, "wb")
        downloaded_file_size = 1
        data = client.client_socket.recv(BUFFER_SIZE)
        
        while data.find(b"FINISHED") == -1:
            file.write(data)
            downloaded_file_size = os.path.getsize(filename)
            data = client.client_socket.recv(BUFFER_SIZE)

        data = data.replace(b"FINISHED",b"")
        file.write(data)
        file.close()  # Close file
        end_time = time.time() - start_time  # Calculate transfer time
        
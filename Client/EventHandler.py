import json
from FileController import *
from PyQt5 import QtWidgets
import os

class EventHandler:
    def __init__(self, client):
        """!
        The constructor of the event handler, setup variables and an array of ui elements

        @param client class: The client class
        """
        self.client = client
        self.ui = client.ui
        self.path = "Files/"
        self.index = 0
        
        self.filePackageArray = [FilePackage(self.ui.deleteButton1, self.ui.downloadButton1, self.ui.filePic1, self.ui.fileName1, self.ui.line1, self),
                                FilePackage(self.ui.deleteButton2, self.ui.downloadButton2, self.ui.filePic2, self.ui.fileName2, self.ui.line2, self),
                                FilePackage(self.ui.deleteButton3, self.ui.downloadButton3, self.ui.filePic3, self.ui.fileName3, self.ui.line3, self),
                                FilePackage(self.ui.deleteButton4, self.ui.downloadButton4, self.ui.filePic4, self.ui.fileName4, self.ui.line4, self),
                                FilePackage(self.ui.deleteButton5, self.ui.downloadButton5, self.ui.filePic5, self.ui.fileName5, self.ui.line5, self),
                                FilePackage(self.ui.deleteButton6, self.ui.downloadButton6, self.ui.filePic6, self.ui.fileName6, self.ui.line6, self),
                                FilePackage(self.ui.deleteButton7, self.ui.downloadButton7, self.ui.filePic7, self.ui.fileName7, self.ui.line7, self)]
        
        self.ui_activation(True)
        
    def get_socket(self, socket):
        """!
        Get the client socket from the client class

        @param socket socket: The client socket
        """
        self.clientSocket = socket

    def register_events_handlers(self):
        """!
        Conncet all the buttons event to their appropriate function
        """
        self.ui.nextButton.clicked.connect(self.connect_wrapper)
        self.ui.upButton.clicked.connect(self.page_up)
        self.ui.downButton.clicked.connect(self.page_down)
        self.ui.backButton.clicked.connect(self.folder_back)
        self.ui.btnCreateFolder.clicked.connect(self.show_folder_naming)
        self.ui.confirmName.clicked.connect(self.create_folder)
        self.ui.addFile.clicked.connect(self.upload_file)

    def connect_wrapper(self):
        """!
        Wrapper for the connect function for disabling lineEdit accordingly
        """

        self.ui.lineEditPassword.setEnabled(False)
        self.ui.lineEditIP.setEnabled(False)

        self.client.connect()

        self.ui.lineEditPassword.setEnabled(True)
        self.ui.lineEditIP.setEnabled(True)

    def folder_back(self):
        """!
        Go back to the last folder, if this is the root directory do nothing
        """
        if self.path == "Files/":
            return

        self.path = self.path[:-1]

        index = self.path.rfind("/")
        self.path = self.path[:index + 1]

        self.request_files(self.path)

    def show_folder_naming(self):
        """!
        Turn on or off the visibility of the line edit for folder naming in the ui
        """
        if self.ui.folderName.isVisible():
            self.ui.folderName.setText("")
            self.ui.folderName.setVisible(False)
            self.ui.confirmName.setVisible(False)
        else:
            self.ui.folderName.setVisible(True)
            self.ui.confirmName.setVisible(True)

    def create_folder(self):
        """!
        Tell the server to create a folder with the desired name
        """
        name = self.ui.folderName.text()

        if len(name) > 50 or len(name) <= 0:
            self.display_message_box("Error creating folder", "The name is too long [50 characters] or empty")
            return

        if name.find("/") != -1 or name.find("\\") != -1 or name.find(":") != -1 or name.find("*") != -1 or name.find("?") != -1 or name.find("\"") != -1 or name.find("<") != -1 or name.find(">") != -1 or name.find("|") != -1:
            self.display_message_box("Folder name", "Name can't contain any of the following characters: \\ / : * ? \" < > |")
            return
        
        self.clientSocket.send(("CREATEFOLDER" + name).encode())

        self.clientSocket.send(self.path.encode())

        if self.clientSocket.recv(15).decode() == "SUCCESS":
            self.request_files(self.path)
        
        else:
            self.display_message_box("Error creating folder", "Error creating this folder, please try to recreate it with a different name")

    def delete_folder(self, path):
        """!
        Ask the server to delete a folder

        @param path str: The path of the folder to delete
        """
        self.clientSocket.send(("DELETEFOLDER" + path).encode())

        if self.clientSocket.recv(15).decode() == "FAILED":
            self.display_message_box("Error deleting folder", "Something went wrong with deleting this folder, please try again")
            return

        self.request_files(self.path)

    def delete_file(self, path):
        """!
        Ask the server to delete a file

        @param path str: The path of the file to delete
        """
        self.clientSocket.send(("DELETEFILE" + path).encode())

        if self.clientSocket.recv(15).decode() == "FAILED":
            self.display_message_box("Error deleting file", "Something went wrong with deleting this file, please try again")
            return

        self.request_files(self.path)


    def request_files(self, directory):         
        """!
        Request the specified directory from the server

        @param directory str: The specified directory
        """
        self.index = 0 
        self.files = []
        self.remove_files_from_packages()

        self.clientSocket.send(("GETDIRECTORY" + directory).encode())
        
        try:
            self.files = json.loads(self.clientSocket.recv(1024).decode())
        except:
            raise Exception("EventHandler", "Couldnt get file list")

        for x in range(len(self.files)):
            self.files[x] = File(self.files[x])

        self.update_file_package()

    def update_file_package(self):
        """!
        Update the array of ui elements with the appropriate files
        """
        i = 0
        for x in range(self.index, self.index + 7):
            try:
                self.filePackageArray[i].set_file(self.files[x])
                i += 1
            except:
                break

        self.update_ui_files()

    def update_ui_files(self):
        """!
        Toggle visibility of ui elements by how many files are in the current page
        """
        for x in range(7):
            self.filePackageArray[x].visibility(True)
        
        for x in self.filePackageArray:
            if x.file == None:
                x.visibility(False)

    def ui_activation(self, state):
        """!
        Toggle the ui visibility by the given state

        @param state bool: The given state of visibility
        """
        for x in self.filePackageArray:
            x.ui_activation(state)

    def page_up(self):
        """!
        Up the file array index and go up a page, if this is the top page do nothing
        """
        if self.index == 0:
            return

        self.remove_files_from_packages()
        self.index = self.index - 7
        self.update_file_package()

    def page_down(self):
        """!
        Down the file array index and go down a page, if this is the bottom page do nothing
        """
        for x in self.filePackageArray:
            if x.file == None:
                return
        
        self.remove_files_from_packages()
        self.index = self.index + 7
        self.update_file_package()


    def download_file(self, file):
        """!
        Download a file from the server

        @param file file: Has the name, extension and path of the file to download
        """
        if file.fileExt == "folder":
            fname = QtWidgets.QFileDialog.getSaveFileName(caption = "Save folder", filter = "ZIP (*.zip)")[0]
        else:
            fname = QtWidgets.QFileDialog.getSaveFileName(caption = "Save file", filter = file.fileExt.upper() + " (*." + file.fileExt + ")")[0]
            
        if fname == "":
            return

        self.ui.progressBar.setEnabled(True)
        self.ui_activation(False)

        if file.fileExt == "folder":
            self.clientSocket.send(("GETFOLDER" + file.filePath).encode())
        else:
            self.clientSocket.send(("GETFILE" + file.filePath).encode())

        decode = ""
        size = int(self.clientSocket.recv(255).decode())
        self.clientSocket.send("READY".encode())
        with open(fname, 'wb') as file:
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

                self.ui.progressBar.setValue(os.path.getsize(fname)/size*100)

        self.ui.progressBar.setValue(100)
        file.close()
        self.ui.progressBar.setEnabled(True)
        self.ui_activation(True)

    def upload_file(self):
        """!
        Upload a file from the server using the file dialog
        """
        fname = QtWidgets.QFileDialog.getOpenFileName(caption = "Select file", filter = "All (*.*)")[0]
        if fname == "":
            return
        nameIndex = fname.rfind("/") + 1

        self.clientSocket.send(("UPLOADFILE" + self.path + fname[nameIndex:]).encode())

        self.ui_activation(False)

        try:
            file = open(fname, 'rb')
            
            l = file.read(1024)
            while(l):
                self.clientSocket.send(l)
                l = file.read(1024)

            file.close()    
            self.clientSocket.send("FINISHEDHOST+".encode())
        except Exception as e:
            self.display_message_box("Error with file upload", "An unexpected error occured while uploading this file (maybe try to rename it?)")   
            print(e)

        self.clientSocket.settimeout(None)
        self.clientSocket.recv(25)
        self.clientSocket.settimeout(4)

        self.request_files(self.path)

        self.ui_activation(True)

    def remove_files_from_packages(self):
        """!
        Remove all the files from the file package array
        """
        for x in self.filePackageArray:
            x.remove_file()

    def display_message_box(self, title, content):
        """!
        Display a message box with the given title and content text

        @param title str: The title of the message box
        @param content str: The content for the message box
        """
        msgBox = QtWidgets.QMessageBox()
        msgBox.setText(content)
        msgBox.setWindowTitle(title)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()
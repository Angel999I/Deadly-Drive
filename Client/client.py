r"""
                            client.py

Description: Client for the downloading server

I/O Input: Information from server, Output: File 

Programmer: Omer Benisty

 _____     ______     ______     _____     __         __  __    
/\  __-.  /\  ___\   /\  __ \   /\  __-.  /\ \       /\ \_\ \   
\ \ \/\ \ \ \  __\   \ \  __ \  \ \ \/\ \ \ \ \____  \ \____ \  
 \ \____-  \ \_____\  \ \_\ \_\  \ \____-  \ \_____\  \/\_____\ 
  \/____/   \/_____/   \/_/\/_/   \/____/   \/_____/   \/_____/ 
                                                                
"""

from socket import *
from enum import Enum
import time
import sys
import os
import ui
from PyQt5 import QtCore, QtGui, QtWidgets
from threading import Thread, active_count

PORT = 6969                 # Set the desired port
BUFFER_SIZE = 1024 * 1000   # Set the buffer size for out packet data  

class Page(Enum):
    connection = 0
    ip = 1
    login = 2
    register = 3
    files = 4

class client:
    def __init__(self):
        if not os.path.exists("Files"):
            os.mkdir("Files")
        if not os.path.exists("Config"):
            os.mkdir("Config")

        self.init_ui()

    def connect(self, address):     
        self.client_socket = socket(AF_INET, SOCK_STREAM)  # Define client socket for socket work
        try:
            self.client_socket.connect(address)  # Connect to our ADDRESS which is our server
        except:
            try:
                os.remove("ConfigDEFAULT_IP.txt")
            except:
                pass
            return False
             
        return True

    def init_ui(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = ui.Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.ui.stacked_widget.setCurrentIndex(Page.connection.value)
        self.MainWindow.show()
        self.event_handler = event_handler(self)
        sys.exit(self.app.exec_())

class event_handler:
    def __init__(self, client):
        self.client = client
        self.ui = client.ui

        self.ui.ip_button_next.clicked.connect(self.connect_ip)
        self.ui.login_button_next.clicked.connect(self.login)
        self.ui.login_button_account.clicked.connect(self.register_page)
        self.ui.register_button_login.clicked.connect(self.login_page)
        self.ui.register_button_next.clicked.connect(self.register)
        self.ui.files_line_edit_commands.returnPressed.connect(self.send_command)

        try:
            file = open("Config/DEFAULT_IP.txt", "r")
        except:
            self.ui.stacked_widget.setCurrentIndex(Page.ip.value)
            return

        address = (file.read(), PORT)
        file.close()

        if self.client.connect(address):
            self.ui.stacked_widget.setCurrentIndex(Page.login.value)
        else:
            self.ui.stacked_widget.setCurrentIndex(Page.ip.value)
            self.ui.ip_line_edit_ipaddress.setPlaceholderText("  Failed to connect")

    def send_command(self):
        command = self.ui.files_line_edit_commands.text()
        command = command.lower()
        
        if command == 'exit':
            try:
                self.client.client_socket.send(command.encode())
            except:
                sys.exit()
            sys.exit()

        elif command == 'dir':
            try: 
                self.client.client_socket.send(command.encode())
                dirs = self.client.client_socket.recv(500).decode()
                if dirs != "EMPTY":
                    self.ui.files_text_edit_console.append(dirs)
                self.ui.files_line_edit_commands.setText("")
            except:
                sys.exit()

        elif command[:8] == 'download':
                self.client.client_socket.send(command.encode())
                self.ui.files_line_edit_commands.setText("")
                self.download_file(command[9:])

        elif command == 'upload':

                filename = QtWidgets.QFileDialog.getOpenFileName()
                self.client.client_socket.send((command + " " + os.path.basename(filename[0])).encode())
                self.ui.files_line_edit_commands.setText("")
                self.upload_file(filename[0])


        elif command == 'test':
            try:
                test = QtWidgets.QFileDialog.getOpenFileName()
                self.client.client_socket.send(("upload " + os.path.basename(test[0])).encode())
                self.ui.files_line_edit_commands.setText("")
                self.upload_file(test[0])
            except:
                sys.exit()

        else:
            self.ui.files_line_edit_commands.setText("")


    def upload_file(self, filename):
        try:
            file = open(filename, "rb")
        except:
            self.client_socket.send("FAILED".encode())
            self.ui.files_text_edit_console.append("\nFile not found")
            return
        
        self.client.client_socket.send(str(os.path.getsize(filename)).encode())

        print(os.path.getsize(filename))

        self.client.client_socket.recv(10)

        try:
            print(self.client.client_socket.sendfile(file, 0))
        except:
            raise Exception("failed uploading file to server")

        file.close()

        self.ui.files_text_edit_console.append("\nFile uploaded succesfully")

    def download_file(self, filename):
        reaction = self.client.client_socket.recv(255).decode()

        if reaction == "FILE NOT FOUND":
            self.ui.files_text_edit_console.append("FILE NOT FOUND")
            return     

        filename = "Files/" + filename

        file_size = int(self.client.client_socket.recv(100))       # Get file size from server
        self.client.client_socket.send("READY FOR FILE".encode())  # Report the server we are ready for file transfer
        start_time = time.time()                            # Start counting down download time

        file = open(filename, "wb")
        downloaded_file_size = 1
        data = self.client.client_socket.recv(BUFFER_SIZE)
        
        while data.find(b"FINISHED") == -1:
            self.progress(downloaded_file_size, file_size)
            file.write(data)
            downloaded_file_size = os.path.getsize(filename)
            data = self.client.client_socket.recv(BUFFER_SIZE)

        data = data.replace(b"FINISHED",b"")
        file.write(data)
        file.close()  # Close file
        self.progress(file_size, file_size)
        end_time = time.time() - start_time  # Calculate transfer time
        self.transfer_summary(end_time)

    def progress(self, count, total):
        value = int((count / total) * 100)
        self.ui.files_progress_bar.setValue(value)
        

    def transfer_summary(self, end_time):
        """
        Description: Print a summary on our successful file transfer
        I/O:
            Input: end_time
            Output: end_time. call get_request()
        """

        self.ui.files_text_edit_console.append("Finished\nTime: " + str(end_time) +'\n')
        
        return

    def register(self):
        first_name = self.ui.register_line_edit_first_name.text()    
        last_name = self.ui.register_line_edit_last_name.text()   
        email = self.ui.register_line_edit_email.text()
        password = self.ui.register_line_edit_password.text()

        packet = "REGISTER" + email + "|" + password + "|" + first_name + "|" + last_name
        self.client.client_socket.send(packet.encode())

        response = self.client.client_socket.recv(10).decode()

        if response == "EMAIL":
            self.ui.register_line_edit_email.setText("")
            self.ui.register_line_edit_first_name.setText("")
            self.ui.register_line_edit_last_name.setText("")
            self.ui.register_line_edit_password.setText("")
            
            self.ui.register_line_edit_first_name.setPlaceholderText("  First name")
            self.ui.register_line_edit_last_name.setPlaceholderText("  Last name")
            self.ui.register_line_edit_password.setPlaceholderText("  Password")
            self.ui.register_line_edit_email.setPlaceholderText("  Email is in use")

        elif response == "TRUE":
            self.ui.stacked_widget.setCurrentIndex(Page.files.value)

    def login_page(self):
        self.ui.stacked_widget.setCurrentIndex(Page.login.value)

    def register_page(self):
        self.ui.stacked_widget.setCurrentIndex(Page.register.value)

    def login(self):
        # Get the login data
        email = self.ui.login_line_edit_email.text()
        password = self.ui.login_line_edit_password.text()

        # If the email doesnt content gmail ref
        if email.find('@gmail.com') == -1:
            # Delete the text from the user
            self.ui.login_line_edit_email.setText("")
            self.ui.login_line_edit_password.setText("")

            # Change the placeholders to display an error
            self.ui.login_line_edit_email.setPlaceholderText("  We are accepting only gmail")

            return

        elif password == "":
            # Delete the text from the user
            self.ui.login_line_edit_email.setText("")
            self.ui.login_line_edit_password.setText("")

            # Change the placeholders to display an error
            self.ui.login_line_edit_password.setPlaceholderText("  Password field is empty")

            return

        final_string = email + "EMAIL" + password
        self.client.client_socket.send(final_string.encode())

        response = self.client.client_socket.recv(10).decode()
        if response == "EMAIL":
            self.ui.login_line_edit_email.setText("")
            self.ui.login_line_edit_password.setText("")

            self.ui.login_line_edit_email.setPlaceholderText("  Email not found")
            self.ui.login_line_edit_password.setPlaceholderText("  Password")

        elif response == "PASSWORD":
            self.ui.login_line_edit_email.setText("")
            self.ui.login_line_edit_password.setText("")

            self.ui.login_line_edit_password.setPlaceholderText("  Password is incorrect")
            self.ui.login_line_edit_email.setPlaceholderText("  Email")

        elif response == "TRUE":
            self.ui.stacked_widget.setCurrentIndex(Page.files.value)
        
    def connect_ip(self):
        ip = self.ui.ip_line_edit_ipaddress.text()
        if len(ip.split(".")) != 4:
            self.ui.ip_line_edit_ipaddress.setText("")
            self.ui.ip_line_edit_ipaddress.setPlaceholderText("  IP Structure is not correct")
            return
        else:
            for x in ip.split("."):
                if int(x) > 256 or int(x) < 0:
                    self.ui.ip_line_edit_ipaddress.setText("")
                    self.ui.ip_line_edit_ipaddress.setPlaceholderText("  One of the numbers is out of range")

        file = open("Config/DEFAULT_IP.txt", "w")
        file.write(ip)
        file.close()

        if self.client.connect((ip, PORT)):
            self.ui.stacked_widget.setCurrentIndex(2)
        else:
            self.ui.ip_line_edit_ipaddress.setText("")
            self.ui.ip_line_edit_ipaddress.setPlaceholderText("  Failed to connect")

    def btn_next_event(self):
        print(self.client.MainWindow.sender())
        sys.exit()

client()
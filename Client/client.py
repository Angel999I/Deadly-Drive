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
import ClientUI
import hashlib

from EventHandler import *
from PyQt5 import QtCore, QtGui, QtWidgets
from threading import Thread, active_count

PORT = 6969                  # Set the desired port
BUFFER_SIZE = 1024 * 1000    # Set the buffer size for out packet data  

class Page(Enum):
    login = 0
    ip = 1
    register = 3
    files = 4

class Client:
    def __init__(self):
        """
        Initialize the client and his UI
        """
        
        # If folder does not exist, create it
        if not os.path.exists("Files"):
            os.mkdir("Files")

        # Init User Interface
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = ClientUI.Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        MainWindow.show()

        # Setup UI events 
        self.eventHandler = EventHandler(self)
        self.eventHandler.register_events_handlers()

        sys.exit(app.exec_())

    def connect(self):
        """
        Connect to the given IP and send the given password
        """

        # Empty out the error labels
        self.ui.labelFailIP.setText("")
        self.ui.labelFailPassword.setText("")

        # Get the given IP and password
        ip = self.ui.lineEditIP.text()
        password = self.ui.lineEditPassword.text()

        # If the IP is structurally wrong set the IP error label and try again
        if not validate_ip(ip):
            self.ui.labelFailIP.setText("The IP structure is not correct")
            return

        # If the password is an empty string set the Password error label and try again
        if len(password) == 0:
            self.ui.labelFailPassword.setText("Please enter a password")
            return

        # Create the socket
        self.clientSocket = socket(AF_INET, SOCK_STREAM)  

        # Try to connect to the server, if not set the IP error label
        try:
            self.clientSocket.connect((ip, PORT))  
        except:
            self.ui.labelFailIP.setText("Could not connect")
            self.ui.lineEditIP.setText("")
            return

        # Send to the server the hashed password
        self.clientSocket.send(hashlib.sha256(password.encode()).hexdigest().encode())
        self.clientSocket.settimeout(10)

        # Get response from the server
        response = self.clientSocket.recv(5).decode()

        # If the server response is false tell the user
        if response == "FALSE":
            self.ui.labelFailPassword.setText("The password is wrong")
            self.ui.lineEditPassword.setText("")
            return
        
        # If the server response is true proceed   
        if response == "TRUE":
            self.ui.stackedWidget.setCurrentIndex(1)
            self.eventHandler.get_socket(self.clientSocket)
            self.eventHandler.request_files("/")


def validate_ip(ip):
    """
    Verify if the given string is structurally true as an IP address
    
    Arguments:
        ip {str} -- IP address for checking
    
    Returns:
        True/False -- If the string is an ip address return true otherwise return false
    """
    try:
        if len(ip.split(".")) != 4:
            return False

        for x in ip.split("."):
            if int(x) > 256 or int(x) < 0:
                return False
    except:
        return False
    
    return True

Client()
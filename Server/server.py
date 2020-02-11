r"""
                            server.py

Description: Server for downloading files from a specific directory

I/O Input: Request/Output: The file asked / Information asked

Programmer: Omer Benisty

 _____     ______     ______     _____     __         __  __    
/\  __-.  /\  ___\   /\  __ \   /\  __-.  /\ \       /\ \_\ \   
\ \ \/\ \ \ \  __\   \ \  __ \  \ \ \/\ \ \ \ \____  \ \____ \  
 \ \____-  \ \_____\  \ \_\ \_\  \ \____-  \ \_____\  \/\_____\ 
  \/____/   \/_____/   \/_/\/_/   \/____/   \/_____/   \/_____/ 
                                                                
"""

import os
import pickle
import sys
import time
import smtplib
import uuid
import colorama
import ServerUI
import datetime

#Extended Files
from ClientHandler import *
from EventHandler import *

from socket import *
from threading import Thread, active_count
from urllib.request import urlopen
from PyQt5 import QtCore, QtGui, QtWidgets

HOST = '0.0.0.0'        # Set the server host to any IP adrress
PORT = 6969             # Set the desired port
BUFFER_SIZE = 1024 * 1000

ADDRESS = (HOST, PORT)  # Tuple of IP address and port

class Server:
    def __init__(self):
        """
        Initialize the server and his UI
        """

        # If folder files not exist, create it
        if not os.path.exists("Files"):
            os.mkdir("Files") 

        # Init User Interface
        self.app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = ServerUI.Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        MainWindow.show()

        # Setup UI events 
        self.eventHandler = EventHandler(self)
        self.eventHandler.register_events_handlers()

        sys.exit(self.app.exec_()) 

    def server_execute(self):
        """
        Validate the server password and launch it
        """

        # Get the password from the UI element
        password = self.ui.lineEdit.text()

        # Verify the password length
        if len(password) < 8:
            self.ui.lineEdit.setText("")
            self.ui.lineEdit.setPlaceholderText("   Password too short, at least 8 characters")
            return

        # Save the hashed password
        self.password = hashlib.sha256(password.encode())

        try:
            # Get the machine server ip and show it to the user
            ip = urlopen('http://ip.42.pl/raw').read().decode()
            self.ui.labelIP.setText(ip)
        except:
            self.ui.labelIP.setText("No internet, only local work")

        # Prepare sockets
        self.serverSocket = socket(AF_INET, SOCK_STREAM)  
        self.serverSocket.bind(ADDRESS)                      
        self.serverSocket.listen(2)                             
        
        # Set the status label to "On"
        self.ui.labelStatus.setText("On")

        # Disable the password line edit
        self.ui.lineEdit.setEnabled(False)

        # Start waiting for clients
        Thread(target=self.wait_client, daemon=True).start() 

        self.eventHandler.register_start_button_as_stop()

        # Set the start button text to stop
        self.ui.startButton.setText("Stop") 

    def server_stop(self):

        # Close the server socket
        self.serverSocket.close()

        # Set the ui elements back
        self.ui.lineEdit.setEnabled(True)
        self.ui.labelStatus.setText("Off")
        self.ui.startButton.setText("Start")
        self.ui.labelIP.setText("")

        # Register the stop button as the start button again
        self.eventHandler.register_stop_button_as_start()

    def wait_client(self):
        """
        Wait for a new client and create a ClientHandler for him
        """

        # Wait for a new client and get his information
        while True:       
            clientSocket, clientAddress = self.serverSocket.accept()

            self.write_log(f"{clientAddress} Connected")

            # Create a ClientHandler for this specific client
            Thread(target=ClientHandler(self, self.serverSocket, clientSocket, clientAddress).login_client, daemon=True).start()

    def write_log(self, log):
        """
        Write the attached string in a log file
        
        Arguments:
            log {str} -- The log message
        """

        # Print the log to the console
        print(f"[{datetime.datetime.now()} {log}")

        # Open the log file
        logFile = open("log.log","a")   
        
        # Write the log to the log file
        logFile.write(f"[{datetime.datetime.now()}] {log}")

        # Close the log file
        logFile.close()
 
Server()

        

import sys
import hashlib
import RequestHandler
from threading import Thread, active_count

MAX_REQUEST_LENGTH = 255  # Max file name length for file name transfer

class ClientHandler:
    def __init__(self, server, serverSocket, clientSocket, clientAddress):
        self.server = server
        self.serverSocket = serverSocket
        self.clientSocket = clientSocket
        self.clientAddress = clientAddress
        self.requestHandler = RequestHandler.RequestHandler(self)

    def login_client(self):
        """
        Compare the passwords and response to the client accordingly
        """

        # Get the client hashed password
        try:
            clientResult = self.clientSocket.recv(256).decode()
        except:
            self.server.write_log("Client disconnected in the login proccess")
            self.disconnect()

        # Compare both password and answer the client
        if clientResult != self.server.password.hexdigest():
            self.clientSocket.send("FALSE".encode())

        else:
            self.clientSocket.send("TRUE".encode())
            self.server.write_log(f"{self.clientAddress} Connected")
            self.get_client_request()
            
        
    def get_client_request(self):
        """
        Description: Get client request
        I/O:
            Input: None
            Output: client request
        """
        while True:
            
            try:
                request = self.clientSocket.recv(MAX_REQUEST_LENGTH).decode()
            except:
                self.disconnect()
                self.server.write_log(f"{self.clientAddress} Unexpected exit")          
                sys.exit()

            self.requestHandler.sort_request(request)

    def disconnect(self):
        self.clientSocket.close()

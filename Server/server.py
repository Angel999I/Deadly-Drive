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
import sys
import time
import datetime
import smtplib
import sqlite3
import uuid
import configparser

from socket import *
from colorama import Fore, Back, Style
from colorama import init as colorama
from threading import Thread, active_count
from urllib.request import urlopen

FILE_PATH = os.path.dirname(os.path.abspath(__file__))

MAX_FILE_NAME_LENGTH = 255  # Max file name length for file name transfer

HOST = '0.0.0.0'        # Set the server host to any IP adrress
PORT = 6969  # Set the desired port
BUFFER_SIZE = 1024 * 1000

ADDRESS = (HOST, PORT)  # Tuple of ip address and port

def write_log(log):
    """
    Description: Write log of the server
    I/O:
        Input: log
        Output: Log text file
    """
    
    log_finished = log

    for x in range(0, 100):
        log_finished = log_finished.replace("[" + str(x) + 'm', "")
            
    log_file.write(log_finished + "  [" + str(datetime.datetime.now()) + "]")
    return log

class server:
    def __init__(self):
        # Wait for client
        self.server_socket = socket(AF_INET, SOCK_STREAM)    # Define client socket for socket work
        self.server_socket.bind(ADDRESS)                     # Bind our socket to our address
        self.server_socket.listen(2)                         # Max queue 2
        colorama()                                           # Init colorama fr colored text

        # Server input thread for /exit command
        Thread(target=self.server_input, daemon=True).start()

        # Init database_init
        self.database_init()

        # Make files folder for users files storage
        if not os.path.exists("Files"):
            os.mkdir("Files")

        config = configparser.ConfigParser()

        ip = urlopen('http://ip.42.pl/raw').read().decode()
        config['Vars'] = {'IPAddress': ip}

        with open('config.ini', 'w') as configfile:
            config.write(configfile)     

        # Wait for client connection
        self.wait_client()

    def server_input(self):
        """
        Description: This method runs on a seprate thread, So we can get input from our server terminal
        I/O:
            Input: None
            Output: 
                COMMANDS: /exit Exit the program and close the socket
        """

        while True:
            cmd = input()
            if cmd.lower() == "exit" or cmd.lower() == "/exit":
                log_file.close()
                try:
                    self.client_socket.close()
                except: pass
                try:
                    self.server_socket.close()
                except: pass
                os._exit(1)

    def database_init(self):
        """
        Description: Init database for accounts use
        I/O:
            Input: None
            Output: Print if database was init succesfully
        """
        global sqlite, cursor
        try:
            sqlite = sqlite3.connect(FILE_PATH + "/sqlite/accounts_db.db", check_same_thread=False)
        except:
            print(write_log(f"\n{Fore.RED}Sqlite failed connecting to database_init"))
        
        cursor = sqlite.cursor()

        print(write_log(f"\n{Fore.GREEN}Sqlite initialized"))


    def wait_client(self):
        """
        Description: Wait for a client connection
        I/O:
            Input: None
            Output: client_socket, client_address; Calls to get_client_request()
        """
        print(write_log(f"\n{Fore.RED}[Deadly]{Fore.LIGHTGREEN_EX} Waiting for client...."))
        while True:            
            client_socket, client_address = self.server_socket.accept()

            print(write_log(f"\n{Fore.WHITE}IP: {client_address[0]}\n{Fore.YELLOW}Client connected"))  # Print info on the client connected
            Thread(target=client_handler(client_socket, client_address).login_client).start()  
       
class client_handler:
    def __init__(self, client_socket, client_address):
        # Make the socket and address public through out the class
        self.client_socket = client_socket
        self.client_address = client_address
        Thread(target=self.timeout, daemon=True).start()

    def client_disconnect(self):
        """
        Description: Disconnect from client
        I/O:
            Input: None
            Output: Close the socket and thread
        """

        print(write_log(f"\n{Fore.YELLOW}({self.client_address[0]}) {Fore.RED}Disconnected"))
        try:
            self.client_socket.close()  # Close the socket
        except:
            pass
        sys.exit()  # Close the thread

    def timeout(self):
        time.sleep(10)
        self.client_socket.close()

    def login_client(self):
        """
        Description: Login our client to our database_init
        I/O:
            Input: None
            Output: Register client / Client connected
        """
        
        try:
            userdata = self.client_socket.recv(200).decode().split("EMAIL") # Get our login info from client
        except:
            self.client_disconnect()

        # If login info contained REGISTER, move to register department
        if userdata[0].find("REGISTER") != -1:
            userdata = userdata[0].replace("REGISTER", "")
            self.register_client(userdata)

        # If packet is not valid disconnect
        if len(userdata) < 2:
            self.client_disconnect()
            
        # Search our client loggin info on our database_init
        email = (userdata[0],)
        cursor.execute("SELECT * FROM accounts WHERE email=?", email)

        password = userdata[1]
        db_password = cursor.fetchall()

        # If email not exist, tell client
        if (db_password == []):
            print(write_log(f"\n{Fore.WHITE}IP: {self.client_address[0]}\n{Fore.YELLOW}Logged with wrong email"))
            try:
                self.client_socket.send("EMAIL".encode())
            except:
                self.client_disconnect()
            self.login_client()

        # If password not exist, tell client
        if password != db_password[0][1]:
            print(write_log(f"\n{Fore.WHITE}IP: {self.client_address[0]}\n{Fore.YELLOW}Logged with wrong password"))
            try:
                self.client_socket.send("PASSWORD".encode())
            except:
                self.client_disconnect()           
            self.login_client()

        # Else log in our client 
        else:   
            print(write_log(f"\n{Fore.WHITE}IP: {self.client_address[0]}\n{Fore.YELLOW}Is logged in"))
            try:
                self.client_socket.send("TRUE".encode())
            except:
                self.client_disconnect()

            # Declare his user id from further use
            self.userid = db_password[0][2]

            # Make his unique folder
            if not os.path.exists("Files/" + self.userid):
                os.mkdir("Files/" + self.userid)
            self.get_client_request()

    def register_client(self, userdata):
        """
        Description: Register our client to database_init
        I/O:
            Input: userdata
            Output: Write new user to database_init
        """
        userdata = userdata.split("|")

        cursor.execute("SELECT * FROM accounts WHERE email=?", (userdata[0],))

        db_data = cursor.fetchall() # Get data that is matching the email

        if (db_data != []):
            try: 
                self.client_socket.send("EMAIL".encode())
            except:
                self.client_disconnect()
            self.login_client()

        userid = str(uuid.uuid4()) # Generate userid
        userdata = (userdata[0], userdata[1], userid, userdata[2], userdata[3]) # Make a tuple for all of our user data

        cursor.execute("INSERT INTO accounts VALUES(?,?,?,?,?)", userdata)
        sqlite.commit() # Commit account to database

        try:
            self.client_socket.send("TRUE".encode()) # Send the client a True mark for succesful register
            print(write_log(f"\n{Fore.WHITE}IP: {self.client_address[0]}\n{Fore.YELLOW}Is a new user"))
        except:
            self.client_disconnect()

        self.userid = userid # Make the userid public throughout the whole class

        # Make folder for our client files if its not exists
        if not os.path.exists("Files/" +  self.userid):
            os.mkdir("Files/" +  self.userid)
            self.get_client_request()

        self.get_client_request()
        
    def get_client_request(self):
        """
        Description: Get client request
        I/O:
            Input: None
            Output: client request
        """
        try:
            request = self.client_socket.recv(MAX_FILE_NAME_LENGTH).decode()  # Get file name from client
        except:
            self.client_disconnect()

        if request == "":
            self.client_disconnect()

        self.request_verification(request)

    def request_verification(self, request):
        """
        Description: Act by the client request. Issue a command or start transfering file
        I/O:
            Input: Client request
            Output: 
                COMMAND:
                    /exit: Close the connection and wait for a new client
                    /dir: Send all the file names from the server directory
                FILENAME:
                    Send the file name to upload_file(filename)
        """

        # If the client issued a command, check which command it is
        request_temp = request.lower()
        # If the client typed exit, disconnect from user
        if request_temp == 'exit':
            self.client_disconnect()
        # If the client typed dir, send files list
        elif request_temp == 'dir':
            print(write_log(f"\n{Fore.WHITE}IP: {self.client_address[0]}\n{Fore.YELLOW}Asked for directory: {request}"))
            requests = os.listdir("Files/" + self.userid + "/")
            if requests == []:
                try:
                    self.client_socket.send("EMPTY".encode())
                except:
                    self.client_disconnect()
                self.get_client_request()
            final_file_names = ""
            for name in requests:
                final_file_names += name + "\n"
            try:
                self.client_socket.send(final_file_names.encode())
            except:
                self.client_disconnect()
            self.get_client_request()
        # If the client typed upload, download file from client
        elif request_temp[:6] == 'upload':
            filename = request_temp[7:]
            self.download_file(filename)
        # If the client typed download, upload file to client
        elif request_temp[:8] == 'download':
            self.upload_file(request[9:])   

        else:
            print(write_log(f"\n{Fore.WHITE}IP: {self.client_address[0]}\n{Fore.YELLOW}Executed wrong command: {request}"))
            self.get_client_request()
        
    
    def download_file(self, filename):
        """
        Description: Download file from our client and store it in his userid folder
        I/O:
            Input: filename
            Output: File in userid folder
        """
        try:
            data_temp = self.client_socket.recv(100).decode()
        except:
            self.client_disconnect()
        # If the file is not found in client, report
        if data_temp.find("FAILED") != -1:
            print(write_log(f"\n{Fore.WHITE}IP: {self.client_address[0]}\n{Fore.YELLOW}Tried to upload a file: {filename}"))
            self.get_client_request()

        print(write_log(f"\n{Fore.WHITE}IP: {self.client_address[0]}\n{Fore.YELLOW}Started uploading file: {filename}"))
        # Get ready for downloading the file
        filename = "Files/" + self.userid + "/" + filename
        file = open(filename, "wb")
        file_size = int(data_temp)
        print(file_size)
        downloaded_file_size = 0

        try:
        # Send ready mark
            self.client_socket.send("RDY".encode())
        except:
            self.client_disconnect()

        # Count the time
        start_time = time.time()
        while file_size != downloaded_file_size:
            try:
                timeout = Thread(target=self.timeout,daemon=true)
                timeout.start()
                file.write(self.client_socket.recv(BUFFER_SIZE))
            except:
                self.client_disconnect()
            
            timeout.exit();
            downloaded_file_size = os.path.getsize(filename)

        file.close()

        print(write_log(f"\n{Fore.WHITE}IP: {self.client_address[0]}\n{Fore.YELLOW}Uploaded file successfuly\nTime elapsed: {time.time() - start_time}"))

        self.get_client_request()

    def upload_file(self, filename):
        """
        Description: Read the file from disk and transfer it to client
        I/O:
            Input: filename
            Output: file size, file binary form to client
        """

        try:
            open("Files/" + self.userid + "/" + filename,'rb') # Try to open the desired file
        except:  
            try:                                                  
                self.client_socket.send("FILE NOT FOUND".encode())
            except:
                self.client_disconnect()
            print(write_log(f"\n{Fore.WHITE}IP: {self.client_address[0]}\n{Fore.YELLOW}Issued wrong file name: {filename}"))

            self.get_client_request()

        try:
            self.client_socket.send("SUCCESS".encode())             # Send success note to the client
        except:
            self.client_disconnect()

        file_size = os.path.getsize("Files/" + self.userid + "/" + filename)       # Get the file size
        print(file_size)
        try:
            self.client_socket.send(str(file_size).encode())        # Send the file size to client
        except:
            self.client_disconnect()
                
        print(write_log("\n" + Fore.RED + "Transfer file to: " + Fore.GREEN + self.client_address[0] + 
        Fore.RED + "\nFile name: " + Fore.GREEN + filename +
        Fore.RED + "\nFile size: " + Fore.GREEN + str(file_size) + "\n")) # Give information on the file transfer                                        
        
        try:
            self.client_socket.recv(10)  # Wait for the client to be ready for file transfer
        except:
            self.client_disconnect()

        with open("Files/" + self.userid + "/" + filename,'rb') as file: 
            try:
                self.client_socket.sendfile(file)                                            
            except:
                self.client_disconnect()

        try:
            self.client_socket.send(b"FINISHED")
        
            self.client_socket.recv(10)  # ! For some reason the server is getting additional input, Ignore
        except:
            self.client_disconnect()

        file.close()

        print(write_log(f"\n{Fore.YELLOW}FILE TRANSFERED SUCCESSFULLY"))

        self.get_client_request()

log_file = open("log.log","a")        
server()

        

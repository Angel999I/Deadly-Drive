from LogHandler import *

def download_file(filename):
    """
    Description: Download file from our client and store it in his userid folder
    I/O:
        Input: filename
        Output: File in userid folder
    """
    try:
        data_temp = client_socket.recv(100).decode()
    except:
        client_disconnect()
    # If the file is not found in client, report
    if data_temp.find("FAILED") != -1:
        print(write_log(f"\nIP: {client_address[0]}\nTried to upload a file: {filename}"))
        get_client_request()

    print(write_log(f"\nIP: {client_address[0]}\nStarted uploading file: {filename}"))
    # Get ready for downloading the file
    filename = "Files/" + userid + "/" + filename
    file = open(filename, "wb")
    file_size = int(data_temp)
    print(file_size)
    downloaded_file_size = 0

    try:
    # Send ready mark
        client_socket.send("RDY".encode())
    except:
        client_disconnect()

    # Count the time
    start_time = time.time()
    while file_size != downloaded_file_size:
        try:
            timeout = Thread(target=timeout,daemon=true)
            timeout.start()
            file.write(client_socket.recv(BUFFER_SIZE))
        except:
            client_disconnect()
        
        timeout.exit();
        downloaded_file_size = os.path.getsize(filename)

    file.close()

    print(write_log(f"\nIP: {client_address[0]}\nUploaded file successfuly\nTime elapsed: {time.time() - start_time}"))

    get_client_request()

def upload_file(filename):
    """
    Description: Read the file from disk and transfer it to client
    I/O:
        Input: filename
        Output: file size, file binary form to client
    """

    try:
        open("Files/" + userid + "/" + filename,'rb') # Try to open the desired file
    except:  
        try:                                                  
            client_socket.send("FILE NOT FOUND".encode())
        except:
            client_disconnect()
        print(write_log(f"\nIP: {client_address[0]}\nIssued wrong file name: {filename}"))

        get_client_request()

    try:
        client_socket.send("SUCCESS".encode())             # Send success note to the client
    except:
        client_disconnect()

    file_size = os.path.getsize("Files/" + userid + "/" + filename)       # Get the file size
    print(file_size)
    try:
        client_socket.send(str(file_size).encode())        # Send the file size to client
    except:
        client_disconnect()
            
    print(write_log("\n" + "Transfer file to: " + client_address[0] + 
    "\nFile name: " + filename +
    "\nFile size: " + str(file_size) + "\n")) # Give information on the file transfer                                        
    
    try:
        client_socket.recv(10)  # Wait for the client to be ready for file transfer
    except:
        client_disconnect()

    with open("Files/" + userid + "/" + filename,'rb') as file: 
        try:
            client_socket.sendfile(file)                                            
        except:
            client_disconnect()

    try:
        client_socket.send(b"FINISHED")
    
        client_socket.recv(10)  # ! For some reason the server is getting additional input, Ignore
    except:
        client_disconnect()

    file.close()

    print(write_log(f"\nFILE TRANSFERED SUCCESSFULLY"))

    get_client_request()
import socket
import tqdm
import os

# Set device ip and port
host = "00.00.00.00"
port = 0000

# Buffer size 
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

# Specify the file to send name
filename = "test.txt"

# Get file size
filesize = os.path.getsize(filename)

# Create the client socket
s = socket.socket()

# Connect to server socket
print(f"[+] Connecting to {host}:{port}")
s.connect((host, port))
print("[+] Connected.")

# Send the filename and filesize
s.send(f"{filename}{SEPARATOR}{filesize}".encode())

# Send the file data
progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "rb") as f:
    while True:

        # Read 4096 bytes from the socket (receive) each time
        bytes_read = f.read(BUFFER_SIZE)

        # Check if the file is end
        if not bytes_read:
            break

        # Send the readed bytes
        s.sendall(bytes_read)

        # Update the progress bar
        progress.update(len(bytes_read))
        
# close the socket
s.close()
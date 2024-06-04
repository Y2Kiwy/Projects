import socket
import tqdm
import os

# Set device ip and port
SERVER_HOST = "00.00.00.00"
SERVER_PORT = 0000

# Buffer size 
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

# Create the TCP server socket
s = socket.socket()

# Bind the socket to specified address
s.bind((SERVER_HOST, SERVER_PORT))

# Enable server to accept new connection (no backlog specified)
s.listen()
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")


# If there is new connection, accept it
client_socket, address = s.accept()
print(f"[+] {address} is connected.")

# Receive the file infos through client socket
received = client_socket.recv(BUFFER_SIZE).decode()
filename, filesize = received.split(SEPARATOR)

# In case of abs path, remove it
filename = os.path.basename(filename)

# Convert file size to int
filesize = int(filesize)

# Recive file from socket and write it into the file stream
progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "wb") as f:
    while True:
        # Read 1024 bytes from the socket (receive) each time
        bytes_read = client_socket.recv(BUFFER_SIZE)

        # Check if the file is end
        if not bytes_read:
            break

        # Write recived bytes into the file
        f.write(bytes_read)

        # Update the progress bar
        progress.update(len(bytes_read))

# Close the client socket
client_socket.close()
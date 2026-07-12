# Import Python's socket module to enable network communication.
import socket

# Create a TCP/IP socket using IPv4 addresses.
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the web server "data.pr4e.org" on port 80 (HTTP).
mysock.connect(("data.pr4e.org", 80))

# Create an HTTP GET request asking the server for the file "romeo.txt".
# encode() converts the string into bytes because sockets send bytes, not strings.
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()

# Send the HTTP request to the server.
mysock.send(cmd)

# Print a blank line to make the output easier to read.
print()

# Keep receiving data from the server until there is no more data.
while True:

    # Receive up to 512 bytes of data from the server.
    data = mysock.recv(512)

    # If no data was received, the server has finished sending everything.
    if len(data) < 1:
        break

    # Convert the received bytes into a string and print them.
    print(data.decode())

# Close the network connection.
mysock.close()
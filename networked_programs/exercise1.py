import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

print()
while True:
    data = mysock.recv(512) # receives data in 512-character chunks
    if len(data) < 1:
        break
    print(data.decode(), end='')

mysock.close()
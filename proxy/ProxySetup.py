import socket
import sys
from threading import *

MAX_CONNECTIONS = 100
BUFFER_SIZE = 2**18
CONNECTION_TIMEOUT = 1000000000

listening_port = int(input("Listening port : "))
sock = 0
proxyInternalSocket = 0

def sockClose():
    global sock, proxyInternalSocket
    sock.close()
    proxyInternalSocket.close()
    pass

def init():
    global sock, proxyInternalSocket
    print("Initializing proxy server...")
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        proxyInternalSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('', listening_port))
        sock.listen(MAX_CONNECTIONS)
    except Exception as e:
        print("[-] Error in binding socket to port", e)
        sys.exit(1)
    
    i = 0
    while True:
        try:
            print(i)
            i+=1
            connection, address = sock.accept()
            print("Waiting for connections...")
            data = connection.recv(BUFFER_SIZE)
            print("===> Connected to proxy")
            Thread(parseURL(connection, data, address)).start()
        except KeyboardInterrupt:
            sockClose()

def parseURL(connection, data, address):
    
    try:
        print(data)
        connectRequest = data.decode().split('\n')[0].split(' ')[1].split(':')

        requestedServer = connectRequest[0]
        requestedPort = int(connectRequest[1])
        print(requestedServer, requestedPort)
        proxy(requestedServer, requestedPort, connection, data, address)
    
    except:
        while True:
            try:
                pass
            except KeyboardInterrupt:
                sockClose()

    return

def proxy(requestedServer, requestedPort, connection, data, address):
    try:
        print("Initializing internal proxy socket...")
        proxyInternalSocket.settimeout(CONNECTION_TIMEOUT)
        print(1)
        proxyInternalSocket.connect((requestedServer, 80))
        print(2)
        proxyInternalSocket.sendall('GET / HTTP/1.1\r\n\r\n'.encode())
    except Exception as e:
        print("Error in setting up internal proxy socket", e)
        while True:
            try:
                pass
            except KeyboardInterrupt:
                sockClose()

    print("===> Connection established via proxy")

    while True:
        try:
            response = proxyInternalSocket.recv(BUFFER_SIZE)
            print(response)
            if(len(response) > 0):
                connection.sendall(response)
            else:
                break
        except:
            sockClose()
    
    print("===> Proxy disconnected")
    connection.close()
    # sock.close()
    return

init()

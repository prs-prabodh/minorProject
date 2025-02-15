from sniffer import sniffer as packetHandler
from model import model as ai
import os
import sys
from threading import Thread
import socket
import time

sys.path.append('../')
sys.path.append('/proxy')

MAX_CONNECTIONS = 50
BUFFER_SIZE = 4096
SOCKET_TIMEOUT = 5
DEBUG = True


def parseRequest(request):
    if DEBUG:
        print("Not ready for deployment. Set DEBUG to True!")
        sys.exit(1)

    request = request.decode()
    request = request.split('\n')[-1]
    address = request.split(' ')
    requestType = address[0]
    host = address[1].split(':')[0]
    port = int(address[1].split(':')[1])
    path = address[2]

    request = requestType + ' ' + path + ' HTTP/1.0\r\nHost: ' + host + '\r\n\r\n'
    # print('Request - \n', request, sep='')
    # request = 'GET /api/users/2 HTTP/1.0\r\nHost: www.reqres.in\r\n\r\n'

    return host, port, request.encode()


def proxy_thread(conn, client_addr):

    request = conn.recv(BUFFER_SIZE)
    print(request)

    if DEBUG:
        webserver = 'www.google.co.in'
        port = 80
        request = 'GET / HTTP/1.1\r\n\r\n'.encode()
    else:
        webserver, port, request = parseRequest(request)

    print("Connect to:", webserver, port)

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(SOCKET_TIMEOUT)
        s.connect((webserver, port))
        s.send(request)

        while True:
            data = s.recv(BUFFER_SIZE)
            print("Data received = ", len(data))
            packet = packetHandler.Ether(data)
            packetHandler.wrpcap("raw_data.pcap", packet)
            if DEBUG:
                print("Pcap Written!")

                ###########################################################################################
                ##   Extract CSV file data put into 'packet_data' used below in ai.analyze(packet_data)  ##
                ##   packet_data should be in form of 2D array. [[], [], [], []]                         ##
                ###########################################################################################

            safe = ai.analyze(packet_data)
            time.sleep(2)
            if not safe:
                threat_report = 'Unsafe Packet. Report: \nThreat type - ' + \
                    threat + '\nThreat level - ' + threat_level
                raise Exception(threat_report)

            if (len(data) > 0):
                if(conn):
                    print('Client socket live on server')
                sent = conn.send(data)
                print("Data sent = ", sent)
            else:
                break
        s.close()
        conn.close()
    except socket.error as e:
        if s:
            s.close()
        if conn:
            conn.close()
        print(e)
        return
    except Exception as e:
        s.close()
        conn.close()
        print(e)
        return


def start(port):

    # print(len(sys.argv))
    if DEBUG:
        if (len(sys.argv) < 2):
            print("usage: proxy <port>")
            sys.exit(1)
        port = int(sys.argv[1])

    host = ''

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen(MAX_CONNECTIONS)

    except socket.error as e:
        if s:
            s.close()
        print("Could not open socket:", e)
        sys.exit(1)

    while True:
        try:
            conn, client_addr = s.accept()

            print("===> Connected to client")

            Thread(proxy_thread(conn, client_addr)).start()
        except KeyboardInterrupt:
            s.close()
            sys.exit(0)


if __name__ == '__main__':
    start(int(sys.argv[1]))

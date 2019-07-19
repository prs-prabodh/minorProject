import sys
from proxy import ProxyServer as proxy

LISTENING_PORT = int(sys.argv[1])

if __name__ == "__main__":
    if(len(sys.argv) > 2):
        if(sys.argv[2] == 'tel'):
            proxy.start(LISTENING_PORT, True)
        else:
            print('Invalid Command!')
    else:
        proxy.start(LISTENING_PORT)

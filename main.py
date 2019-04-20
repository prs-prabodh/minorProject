import sys
from proxy import ProxyServer as proxy

LISTENING_PORT = int(sys.argv[1])

if __name__ == "__main__":
    proxy.start(LISTENING_PORT)

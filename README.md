# minorProject
A cloud based cyber immune system based on machine learning techniques

## Usage
* Current Request format in body - GET www.google.co.in:80 /
* Launch - Call `ProxyServer.py` script from proxy with the `port` parameter passed as an argument from terminal
```bash
cd proxy
sudo python3 ProxyServer.py 9876
```
## Dependencies
* Scapy 
```bash
sudo python3 -m pip install --pre scapy[basic]
```
* Sklearn
```bash
sudo python3 -m pip install sklearn
```

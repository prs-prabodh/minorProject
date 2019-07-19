# Minor Project - Mar 2019
A cloud based cyber immune system based on machine learning techniques

## Usage
* Launch - Call `main.py` script with the `port` parameter passed as an argument from terminal
```bash
sudo python3 main.py 9876
```
* Telnet - Call `main.py` script with the `port`  and `tel` parameter passed as an argument from terminal
```bash
sudo python3 main.py 9876 tel
```

* Postman Testing - Send `GET` request to `localhost:port` with body formatted in the following way
```bash
GET www.reqres.in:80 /api/users/2
GET www.google.co.in:80 /
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

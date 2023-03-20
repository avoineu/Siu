import threading
import socket
import json

s = socket.socket()
serveradress = ('localhost', 3000)

request = {
   "request": "subscribe",
   "port": 8888,
   "name": "fun_name_for_the_client",
   "matricules": ["12345", "67890"]
}

with socket.socket() as s:
    s.connect(serveradress)
    s.send(json.dumps(request).encode())
    response = s.recv(2048).decode()

print(response)

with socket.socket() as s:
    s.bind('localhost', 3000)
    s.listen()
    while True : 
        try :
            client, adress = s.accept()
        except :

        response = s.recv(2048).decode()
    
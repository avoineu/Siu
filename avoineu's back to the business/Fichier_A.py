import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host, port =('localhost', 3000)

try :
    s.connect((host,port))
    print("le client arrive...")
    s.listen('')

    data = {"request": "subsrcibe", "port": "3000", "name": "avoineu", "matricules": [21160]}
    data = data.encode("utf8")
    s.sendall(data)

except ConnectionRefusedError :
    print("ERREUR")

finally :
    s.recvfrom(2048)
    s.close()
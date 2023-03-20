import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host, port =('localhost', 3000)

try :
    s.connect((host,port))
    print("le client arrive...")

    data = 'ca marche le reuf'
    data = data.encode("utf8")
    s.sendall(data)

except ConnectionRefusedError :
    print("ERREUR")

finally :
    s.close()
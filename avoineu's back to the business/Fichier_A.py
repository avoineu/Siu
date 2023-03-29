import socket
import json
import time

server_address = ('localhost', 3000)
Variable = True

# Création de la requête de souscription
request = {
    "request": "subscribe",
    "port": 8888,
    "name": "fun_name_for_the_client",
    "matricules": ["12345", "67890"]
}

# Création de la socket et envoi de la requête de souscription au serveur
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.settimeout(0.5)
    try:
        s.connect(server_address)
        s.sendall(json.dumps(request).encode())
        response = s.recv(1024).decode()
        print(response)
    except socket.timeout:
        print("Le temps d'attente pour la connexion est trop long !")

# Création de la socket et écoute sur le port de souscription
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('localhost', 8888))
    s.listen()

    while Variable:
        # Acceptation de la connexion entrante
        client_socket, client_address = s.accept()
        print('Connexion de', client_address)

        # Réception du message envoyé par le serveur
        data = client_socket.recv(1024).decode()
        print('Reçu', repr(data))

        # Analyse du message reçu et envoi de la réponse appropriée
        message = json.loads(data)
        if message['request'] == 'ping':
            response = {"response": "pong"}
            print(response)
            client_socket.sendall(json.dumps(response).encode())

        # Fermeture de la connexion
        client_socket.close()

        Variable = False #pcq la boucle ne veut pas s'arrêter avec ctrl+c. Pq ?
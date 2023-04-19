import socket
import json
import time
import sys
import random

server_address = ('localhost', 3000)
Variable = True

port = int(sys.argv[1])

# Création de la requête de souscription
request = {
    "request": "subscribe",
    "port": port,
    "name": "Ayoubsback-{}".format(port),
    "matricules": ["21160", "20057", str(port)]
}

# Création de la socket et envoi de la requête de souscription au serveur
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.settimeout(5)
    try:
        s.connect(server_address)
        s.sendall(json.dumps(request).encode())
        response = s.recv(1024).decode()
        print(response)
    except socket.timeout:
        print("Le temps d'attente pour la connexion est trop long !")
        pass

# Création de la socket et écoute sur le port de souscription
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('', port))
    s.listen()

    while Variable:
        s.settimeout(5)
            
        try: 
            # Acceptation de la connexion entrante
            client_socket, client_address = s.accept()
            with client_socket:
                def reponse() :
                    chiffre = random.randint(6,8)
                    toile = message['tile']
                    toile[0]= message['tile'][3]
                    toile[1]= message['tile'][0]
                    toile[2]= message['tile'][1]
                    toile[3]= message['tile'][2]
                    jouer = {"tile":toile,"gate":"A" ,"new_position": chiffre}
                    aenvoyer = {"response":"move", "move":jouer, "message":"on s'en fiche"}
                    client_socket.sendall(json.dumps(aenvoyer).encode())

                print('Connexion de', client_address)

                # Réception du message envoyé par le serveur
                data = client_socket.recv(16000).decode()
                print('Reçu', repr(data))

                # Analyse du message reçu et envoi de la réponse appropriée
                message = json.loads(data)
                if message['request'] == 'ping':
                    response = {"response": "pong"}
                    print(response)
                    client_socket.sendall(json.dumps(response).encode())
                elif message['request'] == 'play':
                    reponse()

        except socket.timeout:
            pass

        #Variable = False #Pour arrêter la boucle étant donné qu'on est déja accepté
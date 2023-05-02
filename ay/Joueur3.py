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
    "name": "Arifsback-{}".format(port),
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
            #{"N": false, "E": true, "S": true, "W": true, "item": 18}
            client_socket, client_address = s.accept()
            with client_socket:
                def reponse() :
                    toile = dict(message['state']['tile'])
                    toile['N']= message['state']['tile']['W']
                    toile['E']= message['state']['tile']['N']
                    toile['S']= message['state']['tile']['E']
                    toile['W']= message['state']['tile']['S']
                    position_actuelle = int(message['state']['positions'][message['state']['current']])
                    jouer = {"tile":toile, "gate":"B", "new_position":(position_actuelle)}
                    if message['state']['board'][int(position_actuelle)]['N'] == True and position_actuelle >= 7 and message['state']['board'][int(position_actuelle - 7)]['S'] == True:
                        jouer = {"tile":toile, "gate":"B", "new_position":(position_actuelle - 7)}
                    elif message['state']['board'][int(position_actuelle)]['E'] == True and position_actuelle not in [6,13,20,27,34,41,48] and message['state']['board'][int(position_actuelle+1)]['W'] == True: # a droite
                        jouer = {"tile":toile, "gate":"B", "new_position":(position_actuelle +1)}
                    elif message['state']['board'][int(position_actuelle)]['S'] == True and position_actuelle <= 41 and message['state']['board'][int(position_actuelle + 7)]['N'] == True  :
                        jouer = {"tile":toile, "gate":"B", "new_position":(position_actuelle + 7)}
                    elif message['state']['board'][int(position_actuelle)]['W'] == True and position_actuelle not in [0,7,14,21,28,35,42] and message['state']['board'][int(position_actuelle-1)]['E'] == True : #a gauche
                        jouer = {"tile":toile, "gate":"B", "new_position":(position_actuelle - 1)}
                    else :
                        jouer = {"tile":toile, "gate":"B", "new_position":(position_actuelle)}
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
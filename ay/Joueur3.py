import socket
import json
import time
import sys
import random

def move(tuile, board, position_actuelle) :
    tuile = turn_tuile(tuile,0)
    gate = decider_gate()
    if board[int(position_actuelle)]['N'] == True and position_actuelle >= 7 and board[int(position_actuelle - 7)]['S'] == True:
        jouer = {"tile":tuile, "gate":gate, "new_position":(position_actuelle - 7)}
    elif board[int(position_actuelle)]['E'] == True and position_actuelle not in [6,13,20,27,34,41,48] and board[int(position_actuelle+1)]['W'] == True: #a droite #pour extremité
        jouer = {"tile":tuile, "gate": gate, "new_position":(position_actuelle +1)}
    elif board[int(position_actuelle)]['S'] == True and position_actuelle <= 41 and board[int(position_actuelle + 7)]['N'] == True  :
        jouer = {"tile":tuile, "gate":gate, "new_position":(position_actuelle + 7)}
    elif board[int(position_actuelle)]['W'] == True and position_actuelle not in [0,7,14,21,28,35,42] and board[int(position_actuelle-1)]['E'] == True : #a gauche
        jouer = {"tile":tuile, "gate":gate, "new_position":(position_actuelle - 1)}
    else :
        jouer = {"tile":tuile, "gate":gate, "new_position":(position_actuelle)}
    return jouer

def decider_position(position_actuelle):
    destination = 0
    while True :
        visited = []
        desination_precedente = destination
        visited.append(desination_precedente)
        destination = 6
    return destination

def decider_gate():
    pass
def decider_rotation(board, tuile, position_actuel):
    return random()


def turn_tuile(tuile, number_rotation):
        #toile = dict(message['state']['tile'])
    #toile['N']= message['state']['tile']['W']
    #toile['E']= message['state']['tile']['N']
    #toile['S']= message['state']['tile']['E']
    #toile['W']= message['state']['tile']['S']
    return tuile
def answer(move):
    message = {"response":"move", "move":move, "message":"on s'en fiche"}
    client_socket.sendall(json.dumps(message).encode())

if __name__ == "__main__" : #permet de se lancer que quand c'est pas importé 
    server_address = ('localhost', 3000)
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
        while True:
            s.settimeout(5)
                
            try: 
                # Acceptation de la connexion entrante
                #{"N": false, "E": true, "S": true, "W": true, "item": 18}
                client_socket, client_address = s.accept()
                with client_socket:
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
                        movement = move(message['state']['tile'],message['state']['board'],int(message['state']['current']))
                        answer(movement)

            except socket.timeout:
                pass

        #Variable = False #Pour arrêter la boucle étant donné qu'on est déja accepté



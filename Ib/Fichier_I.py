# import socket
# import json
# import time
# import sys
# import random
# from collections import deque

# server_address = ('localhost', 3000)
# Variable = True

# port = int(sys.argv[1])

# # Création de la requête de souscription
# request = {
#     "request": "subscribe",
#     "port": port,
#     "name": "Mister_Z-{}".format(port),
#     "matricules": ["21160", "20057", str(port)]
# }

# # Création de la socket et envoi de la requête de souscription au serveur
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.settimeout(5)
#     try:
#         s.connect(server_address)
#         s.sendall(json.dumps(request).encode())
#         response = s.recv(1024).decode()
#         print(response)
#     except socket.timeout:
#         print("Le temps d'attente pour la connexion est trop long !")
#         pass

# # Création de la socket et écoute sur le port de souscription
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind(('', port))
#     s.listen()


# def jouer_bfs():
#     # Acceptation de la connexion entrante
#     client_socket, client_address = s.accept()
#     print('Connexion de', client_address)
#     # Parcours en largeur de l'arbre des coups possibles pour trouver un trésor
#     message = json.loads(client_socket.recv(1024).decode())
#     position_actuelle = message['state']['current']
#     remaining = message['state']['remaining']
#     visited = set()
#     queue = deque()
#     queue.append((position_actuelle, []))
#     while queue:
#         pos, path = queue.popleft()
#         if pos in visited:
#             continue
#         visited.add(pos)
#         if pos in remaining:
#             print("Je suis sur un trésor !")
#             moves = path
#             break
#         else:
#             available_moves = []
#             if message['state']['board'][int(pos)]['N'] == True:
#                 available_moves.append((pos - 7, path + ['N']))
#             if message['state']['board'][int(pos)]['E'] == True:
#                 available_moves.append((pos + 1, path + ['E']))
#             if message['state']['board'][int(pos)]['S'] == True:
#                 available_moves.append((pos + 7, path + ['S']))
#             if message['state']['board'][int(pos)]['W'] == True:
#                 available_moves.append((pos - 1, path + ['W']))
#             queue.extend(available_moves)
#     jouer = random.choice(available_moves)
#     print("Je n'ai pas accés au trésor, choix d'une direction aléatoire",jouer['gate'])

#     # Envoyer la réponse au serveur
#     response = {"move": jouer}
#     client_socket.sendall(json.dumps(response).encode())

# # Boucle pour recevoir les messages du serveur
# while True:
#     try:
#         # Acceptation de la connexion entrante
#         client_socket, client_address = s.accept()
#         message = json.loads(client_socket.recv(1024).decode())
#     except socket.timeout:
#         # Si le temps d'attente est dépassé, se désinscrire du serveur et sortir de la boucle
#         print("Le temps d'attente pour la réception des messages est trop long !")
#         break
#     print(message)
#     # Analyse du message reçu et envoi de la réponse appropriée
#     #message = json.loads(message)
#     if message['request'] == 'ping':
#         response = {"response": "pong"}
#         print(response)
#         client_socket.sendall(json.dumps(response).encode())
#     elif message['request'] == 'play':
#         jouer_bfs()
    
#     if message['status'] == 'end':
#         print("Fin du jeu")
#         Variable = False
#         break
#     jouer_bfs()

#     try:
#         jouer_bfs()
#     except socket.timeout:
#         # Si le temps d'attente est dépassé, se désinscrire du serveur et sortir de la boucle
#         print("Le temps d'attente pour la connexion est trop long !")
#         break
#     except KeyboardInterrupt:
#         # Si le programme est interrompu, se désinscrire du serveur et sortir de la boucle
#         print("Interruption par l'utilisateur")
#         break
#     except:
#         # Si une erreur inattendue se produit, se désinscrire du serveur et sortir de la boucle
#         print("Une erreur inattendue s'est produite :", sys.exc_info()[0])
#         break

#     # Envoi de la requête de désinscription au serveur
#     request = {
#         "request": "unsubscribe",
#         "port": port
#     }

#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         s.settimeout(5)
#         try:
#             s.connect(server_address)
#             s.sendall(json.dumps(request).encode())
#             response = s.recv(1024).decode()
#             print(response)
#         except socket.timeout:
#             print("Le temps d'attente pour la connexion est trop long !")
#             pass
#################################################################################
import socket
import json
import time
import sys
import random
from collections import deque

server_address = ('localhost', 3000)
Variable = True

port = int(sys.argv[1])

# Création de la requête de souscription
request = {
    "request": "subscribe",
    "port": port,
    "name": "Mister_Z-{}".format(port),
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

# Fonction pour jouer avec BFS
def jouer_bfs(client_socket, message):
    position_actuelle = message['state']['current']
    remaining = message['state']['remaining']
    visited = set()
    queue = deque()
    queue.append((position_actuelle, []))
    moves = None
    while queue:
        pos, path = queue.popleft()
        if pos in visited:
            continue
        visited.add(pos)
        if pos in remaining:
            print("Je suis sur un trésor !")
            moves = path
            break
        else:
            available_moves = []
            if message['state']['board'][int(pos)]['N'] == True:
                available_moves.append((pos - 7, path + ['N']))
            if message['state']['board'][int(pos)]['E'] == True:
                available_moves.append((pos + 1, path + ['E']))
            if message['state']['board'][int(pos)]['S'] == True:
                available_moves.append((pos + 7, path + ['S']))
            if message['state']['board'][int(pos)]['W'] == True:
                available_moves.append((pos - 1, path + ['W']))
            queue.extend(available_moves)
        if not queue:
            break
    if moves is not None:
        move = moves[0]
    else:
        move = random.choice(['N', 'E', 'S', 'W'])
    print(f"Je me déplace vers {move}")
    response = {
        "response": "move",
        "move": move
    }
    client_socket.sendall(json.dumps(response).encode())

# Création de la socket et écoute sur le port de souscription
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('', port))
    s.listen()

    # Boucle pour recevoir les messages du serveur
    while Variable:
        try:
            # Acceptation de la connexion entrante
            client_socket, client_address = s.accept()
            message = json.loads(client_socket.recv(16000).decode())
        except socket.timeout:
            # Si le temps d'attente est dépassé, se désinscrire du serveur et sortir de la boucle
            print("Le temps d'attente pour la réception des messages est trop long !")
            break
        print(message)
        # Analyse du message reçu et envoi de la réponse appropriée
        if message['request'] == 'ping':
            response = {"response": "pong"}
            print(response)
            client_socket.sendall(json.dumps(response).encode())
            
        elif message['request'] == 'play':
            position_actuelle = message['state']['current']
            remaining = message['state']['remaining']
            visited = set()
            queue = deque()
            queue.append((position_actuelle, []))
            moves = None
            
            while queue:
                pos, path = queue.popleft()
                
                if pos in visited:
                    continue
                
                visited.add(pos)
                
                if pos in remaining:
                    print("Je suis sur un trésor !")
                    moves = path
                    break
                else:
                    available_moves = []
                    current_pos = int(pos)
                    current_board = message['state']['board']
                    current_board_pos = current_board[current_pos]
                    if not current_board_pos.get('visited', False):
                        current_board_pos['visited'] = True
                        if current_board_pos['N']:
                            available_moves.append((current_pos - 7, path + ['N']))
                        if current_board_pos['E']:
                            available_moves.append((current_pos + 1, path + ['E']))
                        if current_board_pos['S']:
                            available_moves.append((current_pos + 7, path + ['S']))
                        if current_board_pos['W']:
                            available_moves.append((current_pos - 1, path + ['W']))
                        queue.extend(available_moves)

                    
                if not queue:
                    break
                
            if moves is not None:
                move = moves[0]
            else:
                move = random.choice(['N', 'E', 'S', 'W'])
                
            print(f"Je me déplace vers {move}")
            
            response = {
                "response": "move",
                "move": move
            }
            
            client_socket.sendall(json.dumps(response).encode())
            
        elif message['status'] == 'end':
            print("Fin du jeu")
            Variable = False
            break



# try:
#     message = json.loads(client_socket.recv(1024).decode())
# except json.JSONDecodeError as e:
#     print(f"Erreur JSON : {e}")
#     # Traitez l'erreur ici
# print(message)

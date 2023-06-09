import socket
import json
import time
import sys
import random

from collections import deque


def move(tuile, board, position_actuelle) :
    tuile = turn_tuile(tuile,decider_rotation())
    gate = decider_gate()
    jouer = {
        "tile":tuile,
        "gate":gate,
        "new_position":decider_position(board,position_actuelle)
        }
    print(jouer)
    return jouer


def decider_position(board, position_actuelle):
    extreme_W = [0,7,14,21,28,35,42]
    extreme_E = [6,13,20,27,34,41,48]
    directions = []
    if board[position_actuelle]['N'] == True and position_actuelle >= 7 and board[position_actuelle-7]['S'] == True : 
        directions.append(position_actuelle -7)
    if board[position_actuelle]['N'] == True and position_actuelle < 7 and board[position_actuelle+42]['S'] == True :
        directions.append(position_actuelle +42)
    if board[position_actuelle]['S'] == True and position_actuelle <= 41 and board[position_actuelle+7]['N'] == True  : 
        directions.append(position_actuelle +7)
    if  board[position_actuelle]['S'] == True and position_actuelle > 41 and board[position_actuelle-42]['N'] == True:
        directions.append(position_actuelle -42)
    if board[position_actuelle]['W'] == True and position_actuelle not in extreme_W and board[position_actuelle-1]['E'] == True:
        directions.append(position_actuelle -1)
    if board[position_actuelle]['W'] == True and  position_actuelle in extreme_W and board[position_actuelle+6]['E'] == True:
        directions.append(position_actuelle +6)
    if board[position_actuelle]['E'] == True and position_actuelle not in extreme_E and board[position_actuelle+1]['W'] == True :
        directions.append(position_actuelle +1)
    if board[position_actuelle]['E'] == True and position_actuelle in extreme_E and board[position_actuelle-6]['W'] == True:
        directions.append(position_actuelle  -6)

    if len(directions) == 0:
        destination = position_actuelle
    else:
        destination = random.choice(directions)

    return destination
# def decider_position(board, position_actuelle):
#     directions = ['N', 'E', 'S', 'W']
#     random.shuffle(directions)
#     for direction in directions:
#         if board[position_actuelle][direction] and not is_wall(position_actuelle, direction):
#             if direction == 'N':
#                 return position_actuelle - 7
#             elif direction == 'E':
#                 return position_actuelle + 1
#             elif direction == 'S':
#                 return position_actuelle + 7
#             elif direction == 'W':
#                 return position_actuelle - 1
#     return position_actuelle  # ne bouge pas si toutes les directions sont bloquées par des murs


# def is_wall(position, direction):
#     if direction == 'N' and position < 7:
#         return True
#     elif direction == 'E' and position % 7 == 6:
#         return True
#     elif direction == 'S' and position > 41:
#         return True
#     elif direction == 'W' and position % 7 == 0:
#         return True
#     return False

# def decider_position(board, position_actuelle):
#     destination = position_actuelle
#     extreme_W = [0,7,14,21,28,35,42]
#     extreme_E = [6,13,20,27,34,41,48]
#     if board[position_actuelle]['N'] == True :
#         if position_actuelle >= 7 and board[position_actuelle-7]['S'] == True :
#             destination = position_actuelle -7
#         elif position_actuelle < 7 and board[position_actuelle+42]['S'] == True :
#             destination = position_actuelle +42
#     elif board[position_actuelle]['S'] == True : 
#         if position_actuelle <= 41 and board[position_actuelle+7]['N'] == True :
#             destination = position_actuelle +7
#         elif  board[position_actuelle]['S'] == True and position_actuelle > 42 and board[position_actuelle-42]['N'] == True:
#             destination = position_actuelle -42
#     elif board[position_actuelle]['W'] == True :
#         if position_actuelle not in extreme_W and board[position_actuelle-1]['E'] == True :
#             destination = position_actuelle -1
#         elif position_actuelle in extreme_W and board[position_actuelle+6]['E'] == True:
#             destination = position_actuelle +6
#     elif board[position_actuelle]['E'] == True :
#         if position_actuelle not in extreme_E and board[position_actuelle+1]['W'] == True :
#             destination = position_actuelle +1
#         elif position_actuelle in extreme_E and board[position_actuelle-6]['W'] == True:
#             destination = position_actuelle  -6
#     return destination

def decider_gate():
    gate_possible = ['A','B','C','D','E','F','G','H','I','J','K','L']
    gate_selected = random.choice(gate_possible)
    return gate_selected 

def decider_rotation():
    return random.randint(0,3)

def turn_tuile(tuile, number_rotation):
    new_tuile = tuile 
    for i in range(number_rotation):
        new_tuile['N'], new_tuile['E'], new_tuile['S'], new_tuile['W'] = new_tuile['W'], new_tuile['N'], new_tuile['E'], new_tuile['S']
    return tuile

def bts_move(board, position_actuelle):
    tuiles_possibles = [
        {"N": False, "E": False, "S": True, "W": True},
        {"N": True, "E": False, "S": True, "W": False},
        {"N": True, "E": False, "S": False, "W": True},
        {"N": False, "E": True, "S": True, "W": False},
        {"N": True, "E": True, "S": False, "W": False},
        {"N": False, "E": True, "S": False, "W": True}
        ]
    directions = ["N", "E", "S", "W"]
    x, y = position_actuelle
    for i, tuile in enumerate(tuiles_possibles):
        if tuile["N"] and y > 0 and board[y-1][x] == 0:
            return (x, y-1)
        elif tuile["E"] and x < len(board[0])-1 and board[y][x+1] == 0:
            return (x+1, y)
        elif tuile["S"] and y < len(board)-1 and board[y+1][x] == 0:
            return (x, y+1)
        elif tuile["W"] and x > 0 and board[y][x-1] == 0:
            return (x-1, y)
        return None
    
def answer(move):
    message = {
        "response":"move",
        "move":move,
        "message":"ca bouge"
        }
    client_socket.sendall(json.dumps(message).encode())

if __name__ == "__main__" : #permet de se lancer que quand c'est pas importé 
    server_address = ('localhost', 3000)
    port = int(sys.argv[1])
    # Création de la requête de souscription
    request = {
        "request": "subscribe",
        "port": port,
        "name": "Je_joue-{}".format(port),
        "matricules": ["21160", "20057", str(port)]
    }
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # Création de la socket et envoi de la requête de souscription au serveur
        s.settimeout(5)
        try:
            s.connect(server_address)
            s.sendall(json.dumps(request).encode())
            response = s.recv(1024).decode()
            print(response)
        except socket.timeout:
            print("Le temps d'attente pour la connexion est trop long !")
            pass
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # Création de la socket et écoute sur le port de souscription
        s.bind(('', port))
        s.listen()
        while True:
            s.settimeout(5)
            try: 
                client_socket, client_address = s.accept() # Acceptation de la connexion entrante
                with client_socket:
                    print('Connexion de', client_address)
                    data = client_socket.recv(16000).decode() # Réception du message envoyé par le serveur
                    #print('Reçu', repr(data))
                    message = json.loads(data) # Analyse du message reçu et envoi de la réponse appropriée
                    if message['request'] == 'ping':
                        response = {"response": "pong"}
                        print(response)
                        client_socket.sendall(json.dumps(response).encode())
                    elif message['request'] == 'play':
                        movement = move(message['state']['tile'],message['state']['board'],int(message['state']['positions'][message['state']['current']]))
                        answer(movement)
            except socket.timeout:
                pass
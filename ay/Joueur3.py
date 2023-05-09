import socket
import json
import time
import sys
import random

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
    destination = position_actuelle
    extreme_W = [0,7,14,21,28,35,42]
    extreme_E = [6,13,20,27,34,41,48]
    if board[position_actuelle]['N'] == True :
        if position_actuelle >= 7 and board[position_actuelle-7]['S'] == True :
            destination = position_actuelle -7
        elif position_actuelle < 7 and board[position_actuelle+42]['S'] == True :
            destination = position_actuelle +42
    elif board[position_actuelle]['S'] == True : 
        if position_actuelle <= 41 and board[position_actuelle+7]['N'] == True :
            destination = position_actuelle +7
        elif  board[position_actuelle]['S'] == True and position_actuelle > 41 and board[position_actuelle-42]['N'] == True:
            destination = position_actuelle -42
    elif board[position_actuelle]['W'] == True :
        if position_actuelle not in extreme_W and board[position_actuelle-1]['E'] == True :
            destination = position_actuelle -1
        elif position_actuelle in extreme_W and board[position_actuelle+6]['E'] == True:
            destination = position_actuelle +6
    elif board[position_actuelle]['E'] == True :
        if position_actuelle not in extreme_E and board[position_actuelle+1]['W'] == True :
            destination = position_actuelle +1
        elif position_actuelle in extreme_E and board[position_actuelle-6]['W'] == True:
            destination = position_actuelle  -6
    return destination

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

def answer(move):
    message = {
        "response":"move",
        "move":move,
        "message":"quoicouwhat"
        }
    return message 

def get_request(): 
    port = int(sys.argv[1])
    request = {
        "request": "subscribe",
        "port": port,
        "name": "Avoinesback-{}".format(port),
        "matricules": ["21160", "20057"]
    }
    return json.dumps(request)

def ping_pong():
    response = {"response": "pong"}
    print(response)
    return(json.dumps(response))

def subscribe_to_server(server_address):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(5)
        try:
            s.connect(server_address)
            s.sendall(get_request().encode())
            response = s.recv(1024).decode()
            #print(response)
        except socket.timeout:
            print("Le temps d'attente pour la connexion est trop long !")
            pass

def process_serveur_message(data):
    print('Reçu', repr(data))
    message = json.loads(data)
    if message['request'] == 'ping':
        return ping_pong().encode()
    elif message['request'] == 'play':
        movement = move(message['state']['tile'], message['state']['board'], int(message['state']['positions'][message['state']['current']]))
        response = answer(movement)
        print('VOICI MON ANSWER   ', json.dumps(response))
        return json.dumps(response).encode()

def start_subscription_server(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', port))
        s.listen()
        while True:
            s.settimeout(5)
            try: 
                client_socket, client_address = s.accept()
                with client_socket:
                    print('Connexion de', client_address)
                    data = client_socket.recv(16000).decode()
                    to_send = process_serveur_message(data)
                    client_socket.sendall(to_send)
            except socket.timeout:
                pass

def main():
    server_address = ('localhost', 3000)
    subscribe_to_server(server_address)
    port = int(sys.argv[1])
    start_subscription_server(port)

if __name__ == "__main__" :
    main()
import pytest
import Joueur3 
import json
from unittest.mock import patch

def test_decider_gate():
    result = Joueur3.decider_gate()
    gate_possible = ['A','B','C','D','E','F','G','H','I','J','K','L']
    assert result in gate_possible

def test_decider_rotation():
    result = Joueur3.decider_rotation()
    assert result >= 0 and result <= 3

def test_turn_tuile():
    tuile = {'N': 'True', 'E': 'False', 'S': 'True', 'W': 'True'}
    number_rotation = 2
    result = Joueur3.turn_tuile(tuile, number_rotation)
    expected_result = {'N': 'True', 'E': 'True', 'S': 'True', 'W': 'False'}
    assert result == expected_result

def test_answer():
    move = {'tile': {'N': False, 'E': True, 'S': False, 'W': True, 'item': None}, 'gate': 'D', 'new_position': 41}
    result = Joueur3.answer(move)
    expected_result = {
        "response": "move",
        "move": move,
        "message": "on s'en fiche"
    }
    assert result == expected_result

def test_deicder_position():
    board = [{"N": False, "E": True, "S": False, "W": False, "item": None}, {"N": False, "E": True, "S": True, "W": True, "item": 13}, {"N": False, "E": True, "S": True, "W": True, "item": 0}, {"N": False, "E": True, "S": True, "W": True, "item": 20}, {"N": False, "E": True, "S": True, "W": True, "item": 1}, {"N": False, "E": True, "S": True, "W": False, "item": None}, {"N": False, "E": False, "S": True, "W": True, "item": None}, {"N": True, "E": False, "S": True, "W": False, "item": None}, {"N": False, "E": False, "S": True, "W": True, "item": None}, {"N": False, "E": True, "S": True, "W": True, "item": 19}, {"N": False, "E": True, "S": True, "W": True, "item": 21}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": True, "E": True, "S": True, "W": False, "item": 2}, {"N": False, "E": False, "S": True, "W": True, "item": 14}, {"N": True, "E": True, "S": True, "W": False, "item": 3}, {"N": True, "E": False, "S": False, "W": True, "item": None}, {"N": False, "E": True, "S": True, "W": True, "item": 4}, {"N": True, "E": False, "S": True, "W": False, "item": None}, {"N": True, "E": False, "S": True, "W": True, "item": 5}, {"N": False, "E": False, "S": True, "W": True, "item": 17}, {"N": False, "E": True, "S": True, "W": True, "item": 23}, {"N": True, "E": False, "S": False, "W": True, "item": None}, {"N": True, "E": False, "S": False, "W": True, "item": None}, {"N": False, "E": False, "S": True, "W": True, "item": None}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": True, "E": True, "S": False, "W": False, "item": None}, {"N": True, "E": True, "S": True, "W": False, "item": 6}, {"N": False, "E": False, "S": True, "W": True, "item": 12}, {"N": True, "E": True, "S": False, "W": True, "item": 7}, {"N": False, "E": True, "S": True, "W": False, "item": 15}, {"N": True, "E": False, "S": True, "W": True, "item": 8}, {"N": True, "E": False, "S": True, "W": False, "item": None}, {"N": True, "E": False, "S": True, "W": True, "item": 9}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": True, "E": False, "S": True, "W": False, "item": None}, {"N": True, "E": False, "S": True, "W": False, "item": None}, {"N": False, "E": True, "S": True, "W": False, "item": None}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": True, "E": False, "S": True, "W": False, "item": None}, {"N": False, "E": True, "S": True, "W": True, "item": 18}, {"N": True, "E": True, "S": False, "W": False, "item": None}, {"N": False, "E": False, "S": True, "W": True, "item": 16}, {"N": True, "E": True, "S": False, "W": True, "item": 10}, {"N": True, "E": True, "S": False, "W": False, "item": None}, {"N": True, "E": True, "S": False, "W": True, "item": 11}, {"N": False, "E": True, "S": True, "W": False, "item": None}, {"N": True, "E": False, "S": False, "W": True, "item": None}]
    position_actuelle = 0
    result = Joueur3.decider_position(board,position_actuelle)
    expected_result = 1
    assert result == expected_result

def test_move():
    tuile = {'N': 'False', 'E': 'False', 'S': 'True', 'W': 'True'}
    board = [{"N": False, "E": True, "S": False, "W": False, "item": None}, {"N": False, "E": True, "S": True, "W": True, "item": 13}, {"N": False, "E": True, "S": True, "W": True, "item": 0}, {"N": False, "E": True, "S": True, "W": True, "item": 20}, {"N": False, "E": True, "S": True, "W": True, "item": 1}, {"N": False, "E": True, "S": True, "W": False, "item": None}, {"N": False, "E": False, "S": True, "W": True, "item": None}, {"N": True, "E": False, "S": True, "W": False, "item": None}, {"N": False, "E": False, "S": True, "W": True, "item": None}, {"N": False, "E": True, "S": True, "W": True, "item": 19}, {"N": False, "E": True, "S": True, "W": True, "item": 21}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": True, "E": True, "S": True, "W": False, "item": 2}, {"N": False, "E": False, "S": True, "W": True, "item": 14}, {"N": True, "E": True, "S": True, "W": False, "item": 3}, {"N": True, "E": False, "S": False, "W": True, "item": None}, {"N": False, "E": True, "S": True, "W": True, "item": 4}, {"N": True, "E": False, "S": True, "W": False, "item": None}, {"N": True, "E": False, "S": True, "W": True, "item": 5}, {"N": False, "E": False, "S": True, "W": True, "item": 17}, {"N": False, "E": True, "S": True, "W": True, "item": 23}, {"N": True, "E": False, "S": False, "W": True, "item": None}, {"N": True, "E": False, "S": False, "W": True, "item": None}, {"N": False, "E": False, "S": True, "W": True, "item": None}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": True, "E": True, "S": False, "W": False, "item": None}, {"N": True, "E": True, "S": True, "W": False, "item": 6}, {"N": False, "E": False, "S": True, "W": True, "item": 12}, {"N": True, "E": True, "S": False, "W": True, "item": 7}, {"N": False, "E": True, "S": True, "W": False, "item": 15}, {"N": True, "E": False, "S": True, "W": True, "item": 8}, {"N": True, "E": False, "S": True, "W": False, "item": None}, {"N": True, "E": False, "S": True, "W": True, "item": 9}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": True, "E": False, "S": True, "W": False, "item": None}, {"N": True, "E": False, "S": True, "W": False, "item": None}, {"N": False, "E": True, "S": True, "W": False, "item": None}, {"N": False, "E": True, "S": False, "W": True, "item": None}, {"N": True, "E": False, "S": True, "W": False, "item": None}, {"N": False, "E": True, "S": True, "W": True, "item": 18}, {"N": True, "E": True, "S": False, "W": False, "item": None}, {"N": False, "E": False, "S": True, "W": True, "item": 16}, {"N": True, "E": True, "S": False, "W": True, "item": 10}, {"N": True, "E": True, "S": False, "W": False, "item": None}, {"N": True, "E": True, "S": False, "W": True, "item": 11}, {"N": False, "E": True, "S": True, "W": False, "item": None}, {"N": True, "E": False, "S": False, "W": True, "item": None}]
    position_actuelle = 0

    with patch('Joueur3.decider_rotation') as mock_decider_rotation, \
         patch('Joueur3.decider_gate') as mock_decider_gate, \
         patch('Joueur3.decider_position') as mock_decider_position:
        mock_decider_rotation.return_value = 2
        mock_decider_gate.return_value = 'E'
        mock_decider_position.return_value = 1

        result = Joueur3.move(tuile, board, position_actuelle)

        expected_result = {
            "tile": {'N': 'True', 'E': 'True', 'S': 'False', 'W': 'False'},
            "gate": 'E',
            "new_position": 1
        }
        assert result == expected_result

def test_get_request():
    arg_mock = ["Joueur3.py","6666"]
    expected_result = {
        "request": "subscribe",
        "port": 6666,
        "name": "Avoinesback-6666",
        "matricules": ["21160","20057"]
    }

    with patch('Joueur3.sys.argv', arg_mock):
        result = Joueur3.get_request()

    assert result == json.dumps(expected_result)

def test_ping_pong():
    result = Joueur3.ping_pong()
    expected_result = json.dumps({"response": "pong"})
    assert result == expected_result
# Clients de Ayoub et Ibrahim pour le PI2CChampionshipRunner

## Introduction

Nous sommes Ayoub Ben Yamoune (`21160`) et Zian Ibrahim (`20057`), et ce projet a été développé dans le cadre de notre cours d'informatique. Notre objectif était de créer un client capable de jouer au jeu du labyrinthe. Vous pouvez trouver plus d'informations sur le labyrinthe et le serveur hôte ici :[fonctionnement du serveur](https://github.com/qlurkin/PI2CChampionshipRunner) et [fonctionnement du labyrinthe](https://github.com/qlurkin/PI2CChampionshipRunner/tree/main/games/labyrinthe).

## Expliquation des bibliothèques utilisées 

1. ``socket`` : Nous avons utilisé la bibliothèque socket pour établir une communication réseau entre notre client et le serveur. Cette bibliothèque nous permet de recevoir les requêtes et les données du jeu envoyées par le serveur, ainsi que d'envoyer nos mouvements en réponse. La connexion réseau est établie via le protocole TCP/IP.

2. ``JSON`` : Étant donné que les messages reçus du serveur sont au format JSON, nous utilisons la bibliothèque JSON pour convertir les objets JSON en objets Python et vice-versa. Cela nous permet d'échanger des informations entre le serveur et notre client de manière efficace.

3. ``sys`` : Nous utilisons la bibliothèque sys pour récupérer le numéro de port spécifié lors de l'exécution du script Python correspondant à notre client. Par exemple, la ligne de code suivante extrait le numéro de port : 
```python
port = int(sys.argv[1])
```
Cette approche nous permet de spécifier différents numéros de port pour exécuter plusieurs instances de notre client et ainsi les faire jouer les uns contre les autres.

4. ``random`` : La bibliothèque random nous permet de générer des valeurs aléatoires, ce qui est très utile dans certaines parties de notre logique de jeu. Cela nous permet donc de prendre des décisions aléatoires lorsque plusieurs options sont disponibles auxquelles notre stratégie n'a pas de réponse. Par exemple, nous utilisons la fonction suivante pour décider de la rotation d'une tuile :
```python
def decider_rotation():
    return random.randint(0,3)
```
5. ``unittest.mock``: Nous utilisons également cette bibliothèque pour importer le décorateur ``@patch`` qui nous permet de remplacer temporairement des objets et des fonctions par des objets simulés appelés "mocks" lors de nos tests. Cela nous permet de contrôler le comportement voulus des objets simulés et de nous assurer que le code est testé de manière isolée. Dans le cas de la fonction ci-dessous, nous simulons les fonctions ``decider_rotation``, ``decider_gate`` et ``decider_position`` :
```python
def test_move():
    tuile ={'N': 'False', 'E': 'False', 'S': 'True', 'W': 'True'}
    board =[{"N": False, "E": True, "S": False, "W": False, "item": None},...]
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
```
6. ``unittest``: Nous utilisons également la bibliothèque ``unittest`` pour utiliser la classe ``unittest.TestCase`` qui fournit de nombreuses méthodes pour effectuer des tests. L'une de ces méthodes est ``assertRaises``, que nous utilisons pour vérifier si une exception spécifiée est levée lors de l'exécution d'un bloc de code. Nous allons utiliser cette méthode dans notre test ci-dessus avec l'exception "IndexError" :
```python
class TestJoueur3(unittest.TestCase):

    @patch('sys.argv', ['Joueur3.py'])
    def test_main_missing_argument(self):
        with self.assertRaises(IndexError):
            Joueur3.main()
```
##  La stratégie 
Pour la stratégie de notre client, nous avons opté pour plusieurs heuristiques afin d'augmenter les chances d'atteindre une tuile contenant le trésor. Notre approche consiste à faire avancer le client d'une case à chaque tour, en espérant qu'il finira par atteindre la tuile souhaitée. Bien que cette stratégie soit assez lente et aléatoire, elle s'est révélée plus performante que de jouer de manière complètement aléatoire et est relativement simple à mettre en œuvre.

##  Organsiation du répertoire
Notre client fonctionnel prêt à jouer est représenté par le fichier ``Joueur3.py``, tandis que notre dossier de tests contient le fichier ``test_Joueur3.py`` regroupant l'ensemble de nos tests. Le fichier ``requirements.txt`` contient toutes les bibliothèques nécessaires au bon fonctionnement du code et des tests. Les dossiers ``ay`` et ``Ib`` correspondent à nos répertoires contenant nos brouillons et évolutions en cours tout au long du projet.

Nous espérons que cette description clarifie notre approche et nos choix de bibliothèques pour ce projet.

N'hésitez pas à nous contacter si vous avez des questions ou des commentaires.
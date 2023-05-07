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

##  La stratégie 
Pour la stratégie de notre client, nous avons opté pour plusieurs heuristiques afin d'augmenter les chances d'atteindre une tuile contenant le trésor. Notre approche consiste à faire avancer le client aussi loin que possible à chaque tour, en espérant qu'il finira par atteindre la tuile souhaitée. Bien que cette stratégie soit assez aléatoire, elle s'est révélée plus performante que de jouer de manière complètement aléatoire et est relativement simple à mettre en œuvre.

Nous espérons que cette description clarifie notre approche et nos choix de bibliothèques pour ce projet.

N'hésitez pas à nous contacter si vous avez des questions ou des commentaires.
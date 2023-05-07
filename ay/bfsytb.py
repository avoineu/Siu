from queue import Queue
adj_list = {
    "A":["B","D"],
    "B":["A","C"],
    "C":["B"],
    "D":["A","E","F"],
    "E":["D","F","G"],
    "F":["D","E","H"],
    "G":["E","H"],
    "H":["G","F"],
}

visited = {}
level = {} #distance dictionnaire
parent = {}
bfs_traversal_output = []
queue = Queue() #crée une fille d'attente vide qui va essayé tout les noeuds un par un

for node in adj_list.keys():
    visited[node] = False #tout les noeuds déja visité
    parent[node] = None #noeud d'ou l'on vient juste avant de passer au suivant
    level[node] = -1 #distance par rapport au noeud de depart 

print(visited)
print(parent)
print(level)

s = "A"
visited[s] = True
level[s] = 0
queue.put(s)

while not queue.empty():
    u = queue.get()
    bfs_traversal_output.append(u)

    for v in adj_list[u] :
        if not visited[v]:
            visited[v] = True 
            parent[v] = u
            level[v] = level[u]+1
            queue.put(v)

print(bfs_traversal_output)
print(level)
print(level["G"])

v = "G"
path = []
while v is not None:
    path.append(v)
    v = parent(v)
path.reverse()
print(path)
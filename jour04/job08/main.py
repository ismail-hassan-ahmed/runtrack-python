# Ouvrir le fichier maze.mz et stocker les données dans une liste de listes
with open('maze.mz') as f:
    maze = [list(line.strip()) for line in f]

# Trouver l'entrée et la sortie
start = (0, 0)
end = (len(maze)-1, len(maze[0])-1)

# Fonction pour trouver le chemin le plus court en utilisant l'algorithme de recherche en largeur
def find_shortest_path(maze, start, end):
    queue = [(start, [start])]
    visited = set()
    while queue:
        (x, y), path = queue.pop(0)
        if (x, y) == end:
            return path
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            newx, newy = x+dx, y+dy
            if 0 <= newx < len(maze) and 0 <= newy < len(maze[0]) and maze[newx][newy] != '#' and (newx, newy) not in visited:
                queue.append(((newx, newy), path+[(newx, newy)]))
                visited.add((newx, newy))
    return None

# Trouver le chemin le plus court dans le labyrinthe
path = find_shortest_path(maze, start, end)

# Marquer les cases du chemin avec 'X' s'il y a un chemin trouvé
if path is not None:
    for x, y in path:
        maze[x][y] = 'X'
else:
    print("Pas de chemin trouvé!")

# Enregistrer le labyrinthe modifié dans un nouveau fichier
with open('maze-out.mz', 'w') as f:
    for row in maze:
        f.write(''.join(row) + '\n')
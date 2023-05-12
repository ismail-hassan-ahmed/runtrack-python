import pygame

pygame.init()

# Définir les dimensions de la fenêtre
WINDOW_SIZE = (600, 600)

# Créer la fenêtre
screen = pygame.display.set_mode(WINDOW_SIZE)

# Nommer la fenêtre
pygame.display.set_caption("TicTacToe1337")

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Grille de jeu
grid = [[None, None, None], [None, None, None], [None, None, None]]

# Tour de jeu
player = "X"

# Fonction pour dessiner la grille de jeu
def draw_grid():
    for i in range(1, 3):
        # Lignes horizontales
        pygame.draw.line(screen, WHITE, (0, i*200), (600, i*200), 5)
        # Lignes verticales
        pygame.draw.line(screen, WHITE, (i*200, 0), (i*200, 600), 5)

# Fonction pour dessiner les symboles des joueurs sur la grille de jeu
def draw_symbols():
    for i in range(3):
        for j in range(3):
            symbol = grid[i][j]
            if symbol == "X":
                pygame.draw.line(screen, WHITE, (j*200+50, i*200+50), (j*200+150, i*200+150), 10)
                pygame.draw.line(screen, WHITE, (j*200+50, i*200+150), (j*200+150, i*200+50), 10)
            elif symbol == "O":
                pygame.draw.circle(screen, WHITE, (j*200+100, i*200+100), 75, 10)

# Fonction pour vérifier si le jeu est terminé
def game_over():
    for i in range(3):
        # Vérifier les lignes
        if grid[i][0] == grid[i][1] == grid[i][2] != None:
            return True
        # Vérifier les colonnes
        if grid[0][i] == grid[1][i] == grid[2][i] != None:
            return True
    # Vérifier les diagonales
    if grid[0][0] == grid[1][1] == grid[2][2] != None:
        return True
    if grid[0][2] == grid[1][1] == grid[2][0] != None:
        return True
    # Vérifier s'il reste des cases vides
    for i in range(3):
        for j in range(3):
            if grid[i][j] == None:
                return False
    # Si toutes les cases sont remplies et personne n'a gagné, le jeu est terminé
    return True

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Récupérer la position de la souris
            x, y = pygame.mouse.get_pos()
            # Convertir la position en coordonnées de grille
            row = y // 200
            col = x // 200
            # Vérifier si la case est libre
            if grid[row][col] == None:
                # Jouer le coup
                grid[row][col] = player
                # Dessiner les symboles des joueurs sur la grille de jeu
                draw_symbols()
                # Vérifier si le jeu est terminé
                if game_over():
                    print("Le jeu est terminé.")
                    running = False
                # Passer au tour suivant
                if player == "X":
                    player = "O"
                else:
                    player = "X"
    # Dessiner la grille de jeu
    draw_grid()
    # Rafraîchir l'affichage
    pygame.display.update()

# Quitter Pygame
pygame.quit()
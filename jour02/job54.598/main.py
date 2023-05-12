import random

class AI_One:
    def __init__(self):
        pass
        
    def think(self, board, color):
        # board est une liste de listes représentant le plateau de jeu
        # color est une chaine de caractères représentant la couleur du joueur
        # ('rouge' ou 'jaune')
        
        # On peut simplement retourner un numéro de colonne aléatoire
        # pour l'instant, comme suit :
        columns = len(board[0])
        return random.randint(0, columns-1)

class AI_Two:
    def __init__(self):
        pass
    
    def think(self, board, color):
        # board est une liste de listes représentant le plateau de jeu
        # color est une chaine de caractères représentant la couleur du joueur
        # ('rouge' ou 'jaune')

        # On peut simplement retourner un numéro de colonne aléatoire
        # pour l'instant, comme suit :
        columns = len(board[0])
        return random.randint(0, columns-1)

def print_board(board):
    # Affichage du plateau de jeu
    for row in board:
        print('|'.join(row))
    print('-----------')

def get_human_move(board, color):
    # Le joueur humain entre la colonne où il veut jouer
    valid_moves = [str(i) for i in range(len(board[0])) if board[0][i] == ' ']
    while True:
        col = input(f"{color}, entrez la colonne où vous voulez jouer ({','.join(valid_moves)}) : ")
        if col in valid_moves:
            return int(col)

def play_move(board, col, player):
    # Le joueur joue dans la colonne choisie, et la pion est placé dans la première case vide
    for row in range(len(board)-1, -1, -1):
        if board[row][col] == ' ':
            board[row][col] = player
            return row
    return -1

def check_win(board, row, col, player):
    # Vérifie si le joueur a gagné en plaçant son pion en (row, col)
    # selon les règles du Connect Four
    def count_direction(dr, dc):
        # Compte le nombre de pions identiques consécutifs dans une direction donnée
        r, c = row, col
        count = 0
        while r >= 0 and r < len(board) and c >= 0 and c < len(board[0]) and board[r][c] == player:
            count += 1
            r += dr
            c += dc
        return count
        
    for dr in range(-1, 2):
        for dc in range(-1, 2):
            if dr == 0 and dc == 0:
                continue
            count = count_direction(dr, dc) + count_direction(-dr, -dc) - 1
            if count >= 4:
                return True
    return False

def is_board_full(board):
    # Vérifie si le plateau de jeu est plein (match nul)
    for col in range(len(board[0])):
        if board[0][col] == ' ':
            return False
    return True

def play_game():
    # Initialisation du plateau de jeu
    rows = 6
    columns = 7
    board = [[' ' for _ in range(columns)] for _ in range(rows)]
    
    # Initialisation des joueurs
    human_player = 'rouge'
    ai_player = 'jaune'
    ai1 = AI_One()
    ai2 = AI_Two()  # Nouvelle instance de la classe AI_Two
    
    # Boucle de jeu
    current_player = human_player
    while True:
        # Affichage du plateau de jeu
        print_board(board)
        
        # Le joueur courant joue un coup
        if current_player == human_player:
            col = get_human_move(board, human_player)
        elif current_player == ai_player:  # Si c'est au tour de l'IA jaune
            col = ai2.think(board, ai_player)  # Utilise AI_Two
        else:
            col = ai1.think(board, current_player)  # Utilise AI_One
        
        # Le pion est placé sur le plateau
        row = play_move(board, col, current_player)
        
        # Vérifie si le joueur a gagné
        if check_win(board, row, col, current_player):
            print(f"{current_player} a gagné !")
            break
        
        # Vérifie si le plateau de jeu est plein
        if is_board_full(board):
            print("Match nul !")
            break
        
        # Passe la main au joueur suivant
        current_player = human_player if current_player == ai_player else ai_player

play_game()
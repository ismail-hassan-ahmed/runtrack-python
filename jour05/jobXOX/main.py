def get_opponent(player):
    """Retourne le joueur opposé"""
    return 'O' if player == 'X' else 'X'

class AI:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def evaluate_board(self, board, player):
        """Évalue l'état du tableau en fonction du joueur"""
        if check_winner(board, player):
            # Si le joueur a gagné, retourner une valeur élevée
            return 1
        elif check_winner(board, get_opponent(player)):
            # Si l'adversaire a gagné, retourner une valeur basse
            return -1
        else:
            # Sinon, retourner une valeur neutre
            return 0

    def minimax(self, board, player, depth):
        """Recherche récursive du meilleur coup avec l'algorithme Minimax"""
        if depth == 0 or check_game_over(board):
            # Si la profondeur maximale est atteinte ou si le jeu est terminé, retourner la valeur d'évaluation
            return self.evaluate_board(board, player)
        
        best_score = float('-inf') if player == 'X' else float('inf')
        
        for row in range(3):
            for col in range(3):
                if board[row][col] == '':
                    # Si la case est vide, jouer un coup et évaluer le résultat
                    board[row][col] = player
                    score = self.minimax(board, get_opponent(player), depth-1)
                    board[row][col] = ''
                    
                    # Mettre à jour le meilleur score en fonction du joueur
                    if player == 'X':
                        best_score = max(best_score, score)
                    else:
                        best_score = min(best_score, score)
        
        # Retourner le meilleur score
        return best_score

    def get_best_move(self, board, player):
        """Retourne le meilleur coup à jouer"""
        best_move = None
        best_score = float('-inf') if player == 'X' else float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == '':
                    # Si la case est vide, jouer un coup et évaluer le résultat
                    board[row][col] = player
                    score = self.minimax(board, get_opponent(player), self.difficulty)
                    board[row][col] = ''
                    
                    # Mettre à jour le meilleur score en fonction du joueur
                    if player == 'X':
                        if score > best_score:
                            best_score = score
                            best_move = (row, col)
                    else:
                        if score < best_score:
                            best_score = score
                            best_move = (row, col)
        # Retourner le meilleur coup
        return best_move

class Game:
    def __init__(self, mode):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.mode = mode
        self.players = ['X', 'O']
        self.current_player = self.players[0]
        self.ai_difficulty = 2 if self.mode == 'single' else None
        self.ai_player = 'O' if self.mode == 'single' else None

    def display_board(self):
        """Affiche le tableau de jeu"""
        for row in self.board:
            print('|'.join(row))
        print()

    def get_player_move(self):
        """Demande au joueur de saisir son coup"""
        while True:
            move = input(f"Joueur {self.current_player}, saisissez votre coup (ligne, colonne) : ")
            try:
                row, col = move.split(',')
                row, col = int(row.strip()), int(col.strip())
                if self.board[row][col] != '':
                    print("La case est déjà occupée. Veuillez choisir une autre case.")
                else:
                    return row, col
            except ValueError:
                print("Mauvaise saisie. Veuillez saisir deux nombres séparés par une virgule (ex: 1,2).")
            except IndexError:
                print("Mauvaise saisie. Veuillez choisir une case valide (ex: 1,2 pour la première ligne, deuxième colonne).")
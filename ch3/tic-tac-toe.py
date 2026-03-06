import random

class Game:

    def __init__(self, player1, player2):
        
        self.player1 = player1 # X
        self.player2 = player2 # O
        
        self.board = [
            [" "," "," "],
            [" "," "," "],
            [" "," "," "]
        ]
    
    def display_board(self):
        for row in self.board:
            print(row) # Im fine with a 3x3 matrix as the display.

    def run(self, log = False):
        
        while True:

            if log:
                self.display_board()
            
            player1_move = self.player1.choose_move(self.board)

            # unpack array. check if move is legal. act accordingly

            row, col = player1_move

            if self.board[row][col] == "X" or self.board[player1_move] == "O"L
                print("Illegal move!")
            else:
                self.board[row][col] = "X"

            # check if game is over using helper func, if so, check who wins

            # ask player 2 for move

            # check if move is legal, act accordingly

            # check if game is over using helper func, if so, check who wins
        

def is_game_over(board):
    
    # check rows

    for row in board:
        if row == ['X','X','X'] or row == ['O','O','O']:
            return True
    
    # check columns

    for col_index in range(3):
        current_column = []
        for row in board:
            current_column.append(row[col_index])
        if current_column == ['X','X','X'] or current_column == ['O','O','O']:
            return True
    
    # check diagnols

    if [board[0][0], board[1][1], board[2],[2]] == ['X','X','X'] or [board[0][0], board[1][1], board[2],[2]]  == ['O','O','O']:
        return True
    
    if [board[0][2], board[1][1], board[2],[0]] == ['X','X','X'] or [board[0][2], board[1][1], board[2],[0]]  == ['O','O','O']:
        return True
    
    return False

class RandomPlayer:

    # init unnecessary

    def choose_move(self, board):
        
        moves = []

        # find all empty spots
        for row in range(3):
            for column in range(3):
                if board[row][column] == " ":
                    moves.append([row,column])
        
        # moves now has all empty coordinates

        # now randomly choose one of those empty coordinates 
        choice_index = random.randint(0, len(moves)-1)

        return moves[choice_index] #return which coordinate should be updated
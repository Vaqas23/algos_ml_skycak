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
                print()
            
            player1_move = self.player1.choose_move(self.board)

            # unpack array. check if move is legal. act accordingly

            row, col = player1_move

            if self.board[row][col] == "X" or self.board[row][col] == "O":
                print("Illegal move!")
            else:
                self.board[row][col] = "X"

            # check if game is over/who wins using helper func

            if is_game_over(self.board) == "X":
                print("Game Over, Player 1 (X) Wins!")
                self.display_board()
                break
            elif is_game_over(self.board) == "O":
                print("Game Over, Player 2 (O) Wins")
                self.display_board()
                break
            elif is_game_over(self.board):
                print("Game Over, Draw!")
                self.display_board()
                break

            # ask player 2 for move

            player2_move = self.player2.choose_move(self.board)

            # unpack array. check if move is legal. act accordingly

            row, col = player2_move

            if self.board[row][col] == "X" or self.board[row][col] == "O":
                print("Illegal move!")
            else:
                self.board[row][col] = "O"

            # check if game is over/who wins using helper func

            if is_game_over(self.board) == "X":
                print("Game Over, Player 1 (X) Wins!")
                self.display_board()
                break
            elif is_game_over(self.board) == "O":
                print("Game Over, Player 2 (O) Wins")
                self.display_board()
                break
            elif is_game_over(self.board):
                print("Game Over, Draw!")
                self.display_board()
                break
        

# returns False is not over, otherwise returns either X or O (however wins)
def is_game_over(board): 
    
    # check rows

    for row in board:
        if row == ['X','X','X']:
            return "X"
        elif row == ['O','O','O']:
            return "O"
    
    # check columns

    for col_index in range(3):
        current_column = []
        for row in board:
            current_column.append(row[col_index])
        if current_column == ['X','X','X']:
            return "X"
        elif current_column == ['O','O','O']:
            return "O"
    
    # check diagnols

    if [board[0][0], board[1][1], board[2][2]] == ['X','X','X']:
        return "X"
    elif [board[0][0], board[1][1], board[2][2]]  == ['O','O','O']:
        return "O"
    
    if [board[0][2], board[1][1], board[2][0]] == ['X','X','X']:
        return "X"
    elif [board[0][2], board[1][1], board[2][0]]  == ['O','O','O']:
        return "O"
    
    # check if there is alteast 1 empty spot. If so, game is not over
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                return False
    
    # No one has won and there are no empty spots left

    return True

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
    

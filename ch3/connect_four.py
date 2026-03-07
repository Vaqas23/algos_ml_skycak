# redo tic-tac-toe game but for connect-four

import random

class Game:

    def __init__(self, player1, player2):

        self.player1 = player1
        self.player2 = player2

        self.board = [
            [" "," ", " ", " ", " ", " ", " "],
            [" "," ", " ", " ", " ", " ", " "],
            [" "," ", " ", " ", " ", " ", " "],
            [" "," ", " ", " ", " ", " ", " "],
            [" "," ", " ", " ", " ", " ", " "],
            [" "," ", " ", " ", " ", " ", " "],
        ]

    def display_board(self):

        for row in self.board:
            print(row)

    def run(self, log = False):

        if (self.player1.strategy_function == manual_strategy_function):
            print("As player 1, you are X. Enter in 1-3 for row or col. You go first. \n")
        
        if (self.player2.strategy_function == manual_strategy_function):
            print("As player 2, you are O. Enter in 1-3 for row or col. You go second. \n")
        
        while True:

            if log:
                self.display_board()
                print()
            
            # ask for player 1 move

            copy_board = [r[:] for r in self.board]  # makes sure cheater_function can't direct adjust board
            player1_move = self.player1.choose_move(copy_board)
    

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
            copy_board = [r[:] for r in self.board] # makes sure cheater_function can't direct adjust board
            player2_move = self.player2.choose_move(copy_board)

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

def is_game_over(board):
    pass

class Player:

    def __init__(self, strategy_function):

        self.strategy_function = strategy_function
    
    def choose_move(self, board):

        return self.strategy_function(board)

def random_strategy_function(board):

        moves = []

        # find all empty spots
        for row in range(6):
            for column in range(7):
                if board[row][column] == " ":
                    moves.append([row,column])
        
        # moves now has all empty coordinates

        # now randomly choose one of those empty coordinates 
        choice_index = random.randint(0, len(moves)-1)

        return moves[choice_index] #return which coordinate should be updated

def manual_strategy_function(board):
    
    while True:
        
        for row in board:
            print(row)
        
        row = int(input("row: "))
        col = int(input("col: "))
        print() # extra space

        if row > 6 or row < 1 or col > 7 or col < 1:
            print("Out of bounds, try again")
        else:
            break

    return [row - 1, col - 1]

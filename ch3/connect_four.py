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
            print("As player 1, you are X. Enter in 1-7 for col. You go first. \n")
        
        if (self.player2.strategy_function == manual_strategy_function):
            print("As player 2, you are O. Enter in 1-7 or col. You go second. \n")
        
        while True:

            if log:
                self.display_board()
                print()
            
            # ask for player 1 move

            copy_board = [r[:] for r in self.board]  # makes sure cheater_function can't direct adjust board
            player1_move_col = self.player1.choose_move(copy_board)


            if self.board[0][player1_move_col] == "X" or self.board[0][player1_move_col] == "O":
                print("Illegal move!")
            else:
                pass # figure out how to put on lowest row

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
            player2_move_col= self.player2.choose_move(copy_board)


            if self.board[0][player2_move_col] == "X" or self.board[0][player2_move_col] == "O":
                print("Illegal move!")
            else:
                pass # figure out how to put on lowest one

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
    pass # figure this out + input only a column, current code allows for positioning anywhere.

class Player:

    def __init__(self, strategy_function):

        self.strategy_function = strategy_function
    
    def choose_move(self, board):

        return self.strategy_function(board)

def random_strategy_function(board):

    moves = []

    # find all columns with atleast one empty spot
    for column in range(7):
            if board[0][column] == " ":
                moves.append([column])
    
    # now randomly choose one of those empty coordinates 
    choice_index = random.randint(0, len(moves)-1)

    return moves[choice_index] # return col

def manual_strategy_function(board):
    
    while True:
        
        for row in board:
            print(row)
        
        col = int(input("col: "))
        print() # extra space

        if col > 7 or col < 1:
            print("Out of bounds, try again")
        else:
            break

    return col - 1

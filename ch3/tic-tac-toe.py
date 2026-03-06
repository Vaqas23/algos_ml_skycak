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

    def make_move(self, player, symbol, log):
        """Helper method to handle a player's move and check if game is over"""
        while True:
            move = player.choose_move(self.board)
            row, col = move
            if self.board[row][col] != " ":
                print("Illegal move! Try again.")
                continue
            self.board[row][col] = symbol
            break
        
        if log:
            self.display_board()
            print()
        
        result = is_game_over(self.board)
        if result == "X":
            print("Game Over, Player 1 (X) Wins!")
            return True
        elif result == "O":
            print("Game Over, Player 2 (O) Wins!")
            return True
        elif result is True:
            print("Game Over, Draw!")
            return True
        return False

    def run(self, log = False):
        if log:
            self.display_board()
            print()
        
        while True:
            if self.make_move(self.player1, "X", log):
                break
            if self.make_move(self.player2, "O", log):
                break
        

# returns False if not over, otherwise returns either X or O (whoever wins), or True for draw
def is_game_over(board): 
    
    # All possible winning lines
    winning_lines = [
        # Rows
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        # Columns
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        # Diagonals
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    
    # Check if any line is three X's or three O's
    for line in winning_lines:
        if line == ['X', 'X', 'X']:
            return "X"
        elif line == ['O', 'O', 'O']:
            return "O"
    
    # Check if there is at least 1 empty spot. If so, game is not over
    for row in board:
        if " " in row:
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
    

player1 = RandomPlayer()
player2 = RandomPlayer()
game = Game(player1,player2)

game.run(log = True)
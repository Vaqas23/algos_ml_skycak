class Game:

    def __init__(self, player1, player2):
        
        self.player1 = player1
        self.player2 = player2
        
        self.board = [
            [" "," "," "],
            [" "," "," "],
            [" "," "," "]
        ]
    
    def display_board(self):
        for row in self.board:
            print(row) # Im fine with a 3x3 matrix as the display.

    def run(self, log = False):
        pass

class RandomPlayer:

    # init unnecessary

    def choose_move(self, board):
        
        move = [0,0]

        # decide

        return move #return which coordinate should be updated
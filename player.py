import random
from game import TicTacToeGame
from copy import deepcopy
class Player:
    def __init__(self, mark):
        self.mark = mark

    def get_move(self, game):
        while True:
            try:
                print("input next move in col, row")
                row, col = input().split(',')
                row = int(row)
                col = int(col)
                if game.position_is_valid(row, col):
                    return (row, col)
                print("You can't go, try again.")
            except : 
                print("Invalid input, try again.")


class AIRandomPlayer:
    def __init__(self, mark):
        self.mark = mark
    
    def get_move(self,game):
        
        availableSpaces = game.getAvailableSpaces()
        return(random.choice(availableSpaces))
    
class peakAheadAI(Player):
    def __init__(self, mark):
        super().__init__(mark)
    def get_move(self,game):
        available_spaces = game.getAvailableSpaces()
        for row, col in available_spaces:
            futureGame = TicTacToeGame()
            futureGame.board = deepcopy(game.board)
            futureGame.board[row][col] = self.mark
            if futureGame.check_win(self.mark):
                return row, col

        return (random.choice(available_spaces))
            

    

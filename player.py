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
        Corners = [
            (0, 0), (0,2), (2,2), (2,0)
            ]
        Edges = [
            (1,2), (0,1), (1,0), (2,1)
            ]
        available_spaces = game.getAvailableSpaces()
        for row, col in available_spaces:
            futureGame = TicTacToeGame()
            futureGame.board = deepcopy(game.board)
            futureGame.board[row][col] = self.mark
            if futureGame.check_win(self.mark):
                return row, col
        for row,col in available_spaces:
            self.mark = 'X'
            futureGame = TicTacToeGame()
            futureGame.board = deepcopy(game.board)
            futureGame.board[row][col] = self.mark
            if futureGame.check_win(self.mark):
                self.mark = 'O'
                return row, col
            self.mark = 'O'
        
        if game.board[1][1] == '_':
            return 1,1

        if len(game.getAvailableSpots(Corners)) > 2:
            return random.choice(game.getAvailableSpots(Corners))

        if game.getAvailableSpots(Edges):
            return random.choice(game.getAvailableSpots(Edges))
    

        return (random.choice(available_spaces))
            

    

from game import TicTacToeGame
from player import Player, peakAheadAI, AIRandomPlayer

def main():
  game = TicTacToeGame()
  players = [
    Player("X"),
    peakAheadAI("O")
  ]

  print("TIC-TAC-TOE!")
  game.reset_board()
  game.print_board()
  while True:
    for player in players:
      row, col = player.get_move(game)
      game.mark_board(player.mark, row, col)
    
      game.print_board()
      if game.check_win ( player.mark ):

        print(f"{player.mark} WINS!")
        print('Lets play again!')
        game.reset_board()
        break
      if len(game.getAvailableSpaces()) == 0:
        print('Its a Tie')
        print('play again?')
        game.reset_board()
        break
  


main()

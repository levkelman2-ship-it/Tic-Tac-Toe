from game import TicTacToeGame
from player import Player, peakAheadAI, AIRandomPlayer

def main():
  game = TicTacToeGame()
  players = [
    AIRandomPlayer("X"),
    peakAheadAI("O")
  ]

  print("TIC-TAC-TOE!")
  game.reset_board()
  game.print_board()
  x = 0
  tie = 0
  Xwins = 0
  Owins =0
  while x < 10000:
    for player in players:
      row, col = player.get_move(game)
      game.mark_board(player.mark, row, col)
    
      game.print_board()
      if game.check_win ( player.mark ):
        if player.mark == 'X':
          Xwins =+1
        else:
          Owins +=1
        print(f"{player.mark} WINS!")
        print(f'X:{Xwins} O: {Owins}, tie: {tie}')
        print('Lets play again!')
        game.reset_board()
        break
      if len(game.getAvailableSpaces()) == 0:
        tie +=1
        print('Its a Tie')
        print('play again?')
        game.reset_board()
        break
      x+=1
  


main()

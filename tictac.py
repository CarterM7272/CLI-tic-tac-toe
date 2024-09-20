# TIC TAC TOE CLI APPLICATION

# TODO create function that asks for the users move (will need a while loop to continuously run game until winner or "quit")
# TODO when user inputs his move. CLI responds with overview of the board
# TODO CLI loops over board and has a RANDOM response
# TODO create if statements that determine what will happen to game if there is a connections of 3 responses or if the user types "Quit"
# TODO create "/help" command to tell the user how to interact with the command line
# TODO create try catch blocks determining who's turn it is
# TODO manually print the board to the console

size = 3
players = {1: "X", 2: "O"}


def start_game():
  print("""
       *****     TIC         *****
        ****      TAC        ****
          **        TOE      **
           *          CLI    *
        
        Welcome to this tic-tac-toe CLI game! Not sure how to start? Type /help to get started.
        
        """)
  

  # This creates a function that separates the sections of the game
  def print_board_status():
    board = []
    noRow = 3
    noCol = 3
    for r in range(0, noRow, 1):
      board.append([])
      for c in range(0, noCol, 1):
        board[r].append("*")

      for r in range(0, noRow, 1):
        for c in range(0, noCol, 1):
          print(board[r][c], end = "")
  print()

  def player_input():
    while True:
      try:
        nrow = print(int(f"In which column would you like to place your move?"))
        ncol = print(int(f"In which column would you like to place your move?"))
      except ValueError:
        print("Invalid Entry")
        break
  
  print_board_status()
  player_input()




start_game()
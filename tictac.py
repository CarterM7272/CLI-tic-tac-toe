# TIC TAC TOE CLI APPLICATION

# TODO create function that displays the tic tac toe game title
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
  
def print_board_status(board_status):
    sep = "\n" + "-" * (size * 4 - 3) + "\n"
    print("\n" + sep.join(" | ".join(col) for col in board_status) + "\n")
  
def player_input():
  while True:
      try:
        nrow = print(int(f"In which column would you like to place your move?"))
        ncol = print(int(f"In which column would you like to place your move?"))
      except ValueError:
        print("Invalid Entry")
  
  
  

  # while True:
  #   print("What is your move?")
  #   user_choice = input()
  #   for row in board:
  #     for column in row:
  #       print(user_choice, '')

print_board_status()




start_game()
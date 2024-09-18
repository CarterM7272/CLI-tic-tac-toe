# TIC TAC TOE CLI APPLICATION

# TODO create function that displays the tic tac toe game title
# TODO create function that asks for the users move (will need a while loop to continuously run game until winner or "quit")
# TODO when user inputs his move. CLI responds with overview of the board
# TODO CLI loops over board and has a RANDOM response
# TODO create if statements that determine what will happen to game if there is a connections of 3 responses or if the user types "Quit"
# TODO create "/help" command to tell the user how to interact with the command line

def start_game():
  print("""
       *****     TIC         *****
        ****      TAC        ****
          **        TOE      **
           *          CLI    *
        
        Welcome to this tic-tac-toe CLI game! Not sure how to start? Type /help to get started.
        
        """)
  game_status = []

  while True:
    print("What is your move?")
    user_choice = input()







start_game()
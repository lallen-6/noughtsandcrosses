# Lets us play from the terminal
from noughts_crosses import *
import time
clear_board = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

print('Welcome to noughts and crosses, you are X and I am O')
print('This is our starting board')
print_board(clear_board)
print('When prompted, please select the space you would like to move into')
print('I will play after you. And I will win')

while not game_is_over(clear_board):
    print('Whats your move?')
    player_move = int(input('Move? '))
    select_space(clear_board, player_move, "X")
    print_board(clear_board)
    if not game_is_over(clear_board):
        print('Nice move! Now its my turn!')
        time.sleep(0.5)
        select_space(clear_board, minimax(clear_board, False)[1], "O")
        print_board(clear_board)

if game_is_over(clear_board):
    if evaluate_board(clear_board) == 1:
        print('Contratulations, well played')
    if evaluate_board(clear_board) == -1:
        print('I am just too good, try again next time')
        print(r"""

                                       ._ o o
                                       \_`-)|_
                                    ,""       \
                                  ,"  ## |   ಠ ಠ.
                                ," ##   ,-\__    `.
                              ,"       /     `--._;)
                            ,"     ## /
                          ,"   ##    /


                    """)
    if evaluate_board(clear_board) == 0:
        print('That was close, lets play again')

# what do we need for a tictactoe game ?

# the game needs a board (what is a board ?) (done)
# display the board  (done)
# it is a 2 player game (done)
# user should be able to choose X or O (done)
# the app should be able to put the marker on a ##specific location on the board (done)
#the game should switch between players
#what are results ? win or tie ? (done)
#win can be horizontal,verical or diaginal (done)
#the game should check for Win (done)
#the game should check for free Space (done)
#if there is no winner and there is a free space
##continue playing
#ask for a replay after a result


import random #TO RANDOMLY CHOOSE THE PLAYER WHO PLAYS FIRST
from IPython.display import clear_output

#Function definitions

def display_board(board):
    clear_output()  # This only works in jupyter notebook!

    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


#test_board = ['#','X','O','X','O','X','O','X','O','X']

#display_board(test_board)

def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


# The function to take the marker and put it in the desired position on the board
def place_marker(board, marker, position):
    board[position] = marker


# The function to check the horizontal, vertival and diagonal winning
def win_check(board,mark):

    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal


# The function to decide who playes first randoml
def choose_first():
    if random.randint(0, 1) == 0:#choose a random numnber between 1 and 2
        return 'Player 2'
    else:
        return 'Player 1'



# the function to see if the selected position by player is available or not.
def space_check(board, position):

    return board[position] == ' '


# The function to see if the board is full or not
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True



# The function to take the player's next move(position)
def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))

    return position



# The function to see if the player wants to play or not.
def replay():

    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')




#The actual game play and logic of the game
print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break

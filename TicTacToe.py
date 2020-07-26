board = [' '] * 10
marker = ' '
def display_board():    
    print('\n')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('---+---+---')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---+---+---')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('\n')

def marker_input():
    global marker
    while not marker in ['X', 'O']:
        marker = input('Please choose X or O: ').upper()
        if not marker in ['X','O']:
            print('Invalid input!')
    return marker


def flip_player():
    global marker
    if marker == 'X':
        marker = 'O'
    elif marker == 'O':
        marker = 'X'
    return marker

def position_choice():
    position =  0
    pos_list = list(range(1,10))
    while position not in pos_list or not space_check(position):
        position = int(input('Choose your position: '))
        if position not in pos_list:
            print('Invalid position!')
        elif not space_check(position):
            print('That position is already full!')
    return position

def place_marker(position):
    global board, marker
    board[position] = marker
    display_board()
    
def winner_check():
    global marker
    return (board[1]==board[2]==board[3]==marker or
            board[4]==board[5]==board[6]==marker or
            board[7]==board[8]==board[9]==marker or
            board[7]==board[4]==board[1]==marker or
            board[8]==board[5]==board[2]==marker or
            board[9]==board[6]==board[3]==marker or
            board[7]==board[5]==board[3]==marker or
            board[9]==board[5]==board[1]==marker)

def space_check(position):
    global board
    return board[position] == ' '

def full_board_check():
    global board
    for i in range(1,10):
        if space_check(i):
            return False
    return True


def gameon_choice():
    choice = ' '
    while choice not in ['Y','N']:
        choice = input('Do you want to replay? Y or N: ').upper()
        if choice not in ['Y', 'N']:
            print('Invalid choice!')
    if choice == 'Y':
        return True
    else:
         return False


def play_game():   
    global marker,board        
    game_on = True        
    
    while game_on:            
        marker = marker_input()                   
        pos = position_choice()
        place_marker(pos)                    
        if winner_check():              
            print(f"{marker} won!")
            game_on = gameon_choice()
            if game_on:
                board = [' '] * 10
                marker = ' '
                
        else:
            if full_board_check():
                print("It's a draw")
                game_on = gameon_choice()
                if game_on:
                    board = [' '] * 10
                    marker = ' '
        
        flip_player()              

play_game()














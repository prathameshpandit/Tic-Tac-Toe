def display_board(board):
    print(f'{board[7]}|{board[8]}|{board[9]}')
    print(f'{board[4]}|{board[5]}|{board[6]}')
    print(f'{board[1]}|{board[2]}|{board[3]}')
def player_input():
    marker=input("Please pick your marker ")
    while marker!='X' and marker!='O':
        marker=input('Please pick your marker ')
    if marker=='X':
        player1='X'
        player2='O'
    else:
        player1='O'
        player2='X'
    return (player1,player2)
def place_marker(board, marker, position):
    board[position]=marker
def win_check(board,marker):
    check=False
    if board[1]==board[2]==board[3]==marker:
        check=True
    if board[1]==board[4]==board[7]==marker:
        check=True
    if board[2]==board[5]==board[8]==marker:
        check=True
    if board[3]==board[6]==board[9]==marker:
        check=True
    if board[1]==board[5]==board[9]==marker:
        check=True
    if board[3]==board[5]==board[7]==marker:
        check=True
    if board[4]==board[5]==board[6]==marker:
        check=True
    if board[7]==board[8]==board[9]==marker:
        check=True
    return check
def choose_first():
    if random.randint(1,2)==1:
        return 'Player1'
    else:
        return 'Player2'
def space_check(board, position):
    return board[position]==' '
def full_board_check(board):
    check=True
    for char in board[1:10]:
        check= char=='X' or char=='O'
        if not check:
            break
    return check
def player_choice(board,player):
    position=int(input(f"What is your position? "))
    while position<1 or position>9 or (not space_check(board,position)):
            position=int(input("Choose only from 1-9 which is empty, choose another "))
    place_marker(board,player,position) 
    display_board(board)   
def replay():
    return input("Do you want to play again?")=='Yes'
print("Welcome to Tic-Tac-Toe")
import random
while True:
    (player1,player2)=player_input()
    player_board=[' ']*10
    print(f'Player1 is {player1} and PLayer2 is {player2}')
    current_player=choose_first()
    Players={'Player1':player1,'Player2':player2}
    display_board(player_board)
    print(f'{current_player} will play first')
    while True:
        print(f'{current_player}s Turn')
        player_choice(player_board,Players[current_player])
        if win_check(player_board,Players[current_player]):
            print(f'{current_player} wins the game')
            break
        if full_board_check(player_board):
            print('It is a tie')
            break
        if current_player=='Player1':
            current_player='Player2'
        else:
            current_player='Player1'
    if not replay():
        break
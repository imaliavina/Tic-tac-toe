'''
Создайте программу для игры в ""Крестики-нолики"".
'''


def display_board(board):
    print(board[6]+'|'+board[7]+'|'+board[8])
    print(board[3]+'|'+board[4]+'|'+board[5])
    print(board[0]+'|'+board[1]+'|'+board[2])


def input_player_marker():
    marker = ''
    while marker!='O' and marker!='X':
        marker = input('Player1, please choose the symbol you want, X or O:')
    if marker == 'X':
        player1 = 'X'
        player2 = 'O'
    else:
        player1 = 'O'
        player2 = 'X'
    return (player1, player2)


def input_position(board, k):
    pos = 0
    pos_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if k % 2 == 1:
        name = 'Player1'
    else:
        name = 'Player2'
    while (pos not in pos_list) or (board[pos - 1] != ''):
        if (pos not in pos_list):
            pos = int(input(name + ', ' + 'please enter the number (1-9):'))
        elif board[pos - 1] != '':
            pos = int(input('This place is taken, choose another number:'))
    return pos


def if_won(board, marker):
    if (board[0]==board[1]==board[2]==marker) or board[3]==board[4]==board[5]==marker or \
            board[6]==board[7]==board[8]==marker or board[6]==board[3]==board[0]==marker or \
            board[7]==board[4]==board[1]==marker or board[8]==board[5]==board[2]==marker or\
            board[0]==board[4]==board[8]==marker or board[6]==board[4]==board[2]==marker:
        flag = True
    else:
        flag = False
    return flag


def if_tied(board):
    flag = False
    if '' in board:
        return flag
    elif (not if_won(board, 'X')) and (not if_won(board, 'O')):
        flag = True
    return flag


def main_game():
    board = ['']*9
    display_board(board)
    marker_player1, marker_player2 = input_player_marker()
    k = 1
    tied, won1, won2 = False, False, False
    ans = 'N'

    while (not tied) and (not won1) and (not won2):
        pos = input_position(board, k)
        if k%2==1:
            board[pos-1] = marker_player1
        else:
            board[pos-1] = marker_player2
        display_board(board)
        tied = if_tied(board)
        won1 = if_won(board,marker_player1)
        won2 = if_won(board,marker_player2)
        if tied:
            print("Game over. It's tie")
            ans = input('Do you want to play again: Y/N?')
        elif won1:
            print("Congrats! Player1, you won!")
            ans = input('Do you want to play again: Y/N?')
        elif won2:
            print("Congrats! Player2, you won!")
            ans = input('Do you want to play again: Y/N?')
        if ans=='Y':
            main_game()
        k += 1


main_game()
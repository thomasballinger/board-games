import random


def display_board(board):
    '''Returns a visual representation of the current board'''

    empty_row = '   |   |   '
    token_row = ' {} | {} | {} '
    full_row = '___|___|___'
    template = '\n'.join([empty_row,
                          token_row,
                          full_row,
                          token_row,
                          full_row,
                          token_row,
                          empty_row])
    print()
    print(template.format(*board[1:]))
    print()


def get_move(player, board, piece):
    '''Returns a new move from either player,
    or the computer if a 1 player game'''

    if player in ('Player 1', 'Player 2'):
        move = input("{}, it's your turn. Enter 1-9:\n".format(player))
        while True:
            while True:
                try:
                    move = int(move)
                    break
                except ValueError:
                    move = input("Please enter a number 1-9.\n")
            if move in board:
                return move
            move = int(input("That square is already taken. Try again.\n"))
    elif player == 'Computer':
        return computer_move(board, piece)


def update_board(board, move, piece):
    '''Updates the board with a new move and returns it'''
    board[move] = piece


def check_victory(board, piece):
    '''Checks whether the victory conditions are met for a given player'''

    for s1, s2, s3 in [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],
            [1, 4, 7], [2, 5, 8], [3, 6, 9],
            [1, 5, 9], [3, 5, 7]]:
        if (board[s1] == board[s2] == board[s3] == piece):
            return True
    return False


def play_again():
    '''Returns input from the player whether or not to start a new game'''
    return input('Play again? y/n\n').lower() == 'y'


def one_or_two_players():
    '''Returns input from the player whether to start in 1 or 2 player mode'''
    return 2 if input('One or two players? 1/2\n') == '2' else 1


def play(first_mover):
    '''Function that actually handles playing the game'''

    board = [None] + list(range(1, 10))
    player = first_mover
    while True:
        piece = player_dict[player]
        if player in ('Player 1', 'Player 2'):
            display_board(board)
        move = get_move(player, board, piece)
        update_board(board, move, piece)
        if check_victory(board, piece):
            break
        if not [loc for loc in board if str(loc).isdigit()]:
            display_board(board)
            print('The game ends in a draw.\n')
            if play_again():
                player = invert_dict[player]
                play(player)
            else:
                print('Thanks for playing!')
                return
        player = invert_dict[player]
    display_board(board)
    print('Congratulations {}, you won!\n'.format(player.lower()))
    if play_again():
        player = invert_dict[player]
        play(player)
    else:
        print('Thanks for playing!')
        return


def computer_move(board, piece):
    '''Returns a move for the computer in 1 player mode'''

    invert_piece = {'X': 'O', 'O': 'X'}
    opp_piece = invert_piece[piece]
    transform_sides = {1: 9, 9: 1, 2: 8, 8: 2, 3: 7, 7: 3, 4: 6, 6: 4}
    corners = (1, 3, 7, 9)
    sides = (2, 4, 6, 8)
    board_tuple = tuple(board)
    open_spaces = tuple(loc for loc in board_tuple if str(loc).isdigit())
    for loc in board_tuple:
        if loc in open_spaces:
            test_board = list(board_tuple)
            test_board[loc] = piece
            if check_victory(test_board, piece) == True:
                return loc
    for loc in board_tuple:
        if loc in open_spaces:
            test_board = list(board_tuple)
            test_board[loc] = opp_piece
            if check_victory(test_board, opp_piece) == True:
                return loc
    if len(open_spaces) == 9:
        return 1
    open_corners = [l for l in open_spaces if l in corners]
    open_sides = [l for l in open_spaces if l in sides]
    corners_list = [l for i, l in enumerate(board_tuple) if i in corners]
    sides_list = [l for i, l in enumerate(board_tuple) if i in sides]
    if len(open_spaces) == 8:
        if board_tuple[5] == opp_piece:
            return 1
        else:
            return 5
    if len(open_spaces) == 7:
        if opp_piece in sides_list:
            return 5
        if board_tuple[5] == opp_piece:
            return 9
        if opp_piece in [board_tuple[7], board_tuple[9]]:
            return 3
        if board_tuple[3] == opp_piece:
            return 7
    if len(open_spaces) == 6:
        if board_tuple[1] == opp_piece and board_tuple[9] == opp_piece:
            return 8
        if board_tuple[3] == opp_piece and board_tuple[7] == opp_piece:
            return 8
        if len(open_corners) == 3:
            if opp_piece in corners_list:
                for maybeOpp, response in {1: 9, 3: 7, 7: 3, 9: 1}.items():
                    if board_tuple[maybeOpp] == opp_piece:
                        return response
    if len(open_spaces) == 5:
        if len(open_corners) == 1:
            return open_corners[0]
        if 5 in open_spaces:
            return 5
    if open_corners:
        good_corners = [l for l in open_corners if transform_sides[l]
                        in open_corners]
        if good_corners:
            return random.choice(good_corners)
    if 5 in open_spaces:
        return 5
    good_sides = [l for l in open_sides if transform_sides[l] in open_sides]
    if good_sides:
        return random.choice(good_sides)
    if open_spaces:
        return random.choice(open_spaces)
    else:
        return None


if __name__ == '__main__':
    players = one_or_two_players()
    if players == 2:
        invert_dict = {'Player 1': 'Player 2', 'Player 2': 'Player 1'}
        player_dict = {'Player 1': 'X', 'Player 2': 'O'}
    if players == 1:
        invert_dict = {'Player 1': 'Computer', 'Computer': 'Player 1'}
        player_dict = {'Player 1': 'X', 'Computer': 'O'}
    play('Player 1')



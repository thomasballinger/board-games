def board_maker(x, y):
    '''Returns a board data structure based on the two dimensions passed in'''
    column = [' ' for y in range(y)]
    board = [column for x in range(x)]
    return board


def board_printer(board):
    '''Takes the current board structure and prints it to the terminal'''
    board_width = len(board)
    board_height = len(board[0])
    print('\n')
    for num in range(board_height):
        i = num + 1
        row = [column[-i] for column in board]
        print(row)
    print('\n')
    print([str(i + 1) for i in range(board_width)])
            

def move_getter(player, board):
    player_piece = {'P1': 'X', 'P2': 'O'}
    move = input('{}, type the number of desired column:\n'.format(player))
    move_int = int(move)
    move_index = move_int - 1
    while True:
        if move in [str(i) for i in range(len(board))]:
            if board[move_int][-1] == ' ':
                insert_spot = list(reversed(board[move_int])).index(' ')
                insert_index = -(insert_spot + 1)
                board[move_int][insert_index] = player_piece[player]
                return board, move
            else:
                move = input('That column is full! Pick another:\n')
        else:
            move = input('Please enter a number of a column:\n')
    

def victory_checker(board):
    pass
    # '''Returns True if victory, False if continue, and 'draw' if a tie'''

def draw_checker(board):
    pass
    # check if there are any valid moves remaining
    # return True if there aren't any

def move_recorder(move, move_history):
    pass
    # take the last move and add it to the move history
    # return the new move history




def main():
    pass

# if __name__ == '__main__':
#     main()





'''Function that returns the desired board size
# Function that draws the board for the user
# Function that gets a move and returns it
# Function that adds the move to the board
# Function that checks for victory conditions
# Function that checks for draw conditions
# Function that records the sequence of moves that were made'''

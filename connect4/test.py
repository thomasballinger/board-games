import connect4 as c
import unittest as u

class Tests(u.TestCase):

    def test_board_maker(self):
        pass


if __name__ == '__main__':
    board = [
            ['X', ' ', ' ', ' ', ' '],
            ['X', ' ', ' ', ' ', ' '],
            ['X', 'X', ' ', ' ', ' '],
            ['X', ' ', ' ', ' ', ' '],
            ['X', ' ', ' ', ' ', ' ']
            ]
    # u.main()
    board, move = c.get_move('P1', board)
    print(move)
    c.print_board(board)


# should print a normal board as a list of lists
# board = c.board_maker(5, 5)
# print(board)

# should print a properly displayed 5x5 board with 'X' on bottom row
# board2 = [['X', ' ', ' ', ' ', ' '],
#           ['X', ' ', ' ', ' ', ' '],
#           ['X', 'X', ' ', ' ', ' '],
#           ['X', ' ', ' ', ' ', ' '],
#           ['X', ' ', ' ', ' ', ' ']]
# c.board_printer(board2)

from bisect import insort_left
from functools import partial

from move_notation import index_to_chess
board_struct = {
    'white':
        {
        'pawns': [],
        'rocks': [],
        'queens': [],
        'king': [],
        'bishops': [],
        'knights': [],
        'casteling': []
    },

    'black':
        {
        'pawns': [],
        'rocks': [],
        'queens': [],
        'king': [],
        'bishops': [],
        'knights': [],
        'casteling': [],

    }
}
board = []
for i in range(64):
    if i == 7:
        board.append(1)
        continue
    board.append(0)



# TODO write a function that makes the move
# TODO write a function that translates move notation into changes in the board
def right_edge(board_index):

    one_index = board_index + 1

    if one_index % 8 == 0:
        return True
    else:
        return False

def left_edge(board_index):
    if board_index % 8 == 0:
        return True
    else:
        return False

def top_edge(board_index):


    if board_index < 8:
        return True
    else:
        return False

def down_edge(board_index):

    if board_index > 55:
        return True
    else:
        return False


def check_index():
    return 0 + 2

def pawn_movment(board_index,white):
    if white:
        move_index = board_index

        if board_index > 47 & board_index < 56:
            for i in range(2):
                move_index -=8
    else:
        move_index = board_index
        if board_index > 7 & board_index < 16:
            for i in range(2):
                move_index += 8




def knight_movments(board_index):

    on_top_edge = top_edge(board_index)
    on_down_edge = down_edge(board_index)
    on_left_edge = left_edge(board_index)
    on_right_edge = right_edge(board_index)
    edges = [on_left_edge,on_right_edge,on_top_edge,on_down_edge]


def check_for_piece(piece,white,index):

    if white:
        if board_struct['white'][piece][index] == piece:
            return True
        else:
            return False
    else:
        if board_struct['black'][piece][index] == piece:
            return True
        else:
            return False




def rook_movments(board_index,function,color): # TODO introuduce a paramater that its pinned
    not_on_edge = True
    move_index = board_index
    inner_function_logs = []
    if not_on_edge:  # RIGHT →

        not_on_edge = not right_edge(move_index)
        if not_on_edge:
            move_index += 1
            function()
            # TODO add check_index() function and action

    not_on_edge = True
    move_index = board_index

    if not_on_edge:  # LEFT ←

        not_on_edge = not left_edge(move_index)
        if not_on_edge:
            move_index -= 1

    not_on_edge = True
    move_index = board_index  # reset

    if not_on_edge:  # TOP ↑

        not_on_edge = not top_edge(move_index)
        if not top_edge(move_index):
            move_index -= 8

    not_on_edge = True
    move_index = board_index

    if not_on_edge:  # DOWN ↓

        not_on_edge = not down_edge(move_index)
        if not down_edge(move_index):
            move_index += 8

def bishop_movments(board_index):
    not_on_edge = True
    move_index = board_index
    if not_on_edge:  # RIGHT UP →

        not_on_edge = not (right_edge(move_index) or top_edge(move_index))
        if not_on_edge:
            move_index -= 7

    not_on_edge = True
    move_index = board_index

    if not_on_edge:  # LEFT UP←

        not_on_edge = not (left_edge(move_index) or top_edge(move_index))
        if not_on_edge:
            move_index -= 9

    not_on_edge = True
    move_index = board_index  # reset

    if not_on_edge:  # Down left ↓

        not_on_edge = not (down_edge(move_index) or left_edge(move_index))

        if not_on_edge:
            move_index += 7
            print(move_index)

    not_on_edge = True
    move_index = board_index

    if not_on_edge:  # DOWN Right ↓

        not_on_edge = not (down_edge(move_index) or right_edge(move_index))
        if not_on_edge:
            move_index += 9



print(bishop_movments(22))


def is_check(board,white: bool):
    if white:
        color = "white"
    else:
        color = "black"
    king_index = board[color]['king'].index()




def find_moves(board,castel_rights):
    board_index = 0
    for piece in board:
        move_index = board_index
        if piece == 1: # selects piece to move with in the postion
            pass


        board_index += 1








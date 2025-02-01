fen_example = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
board_struct = {
    'move': 'white',
    'white':
        {
        'pawns': [],
        'rooks': [],
        'queens': [],
        'king': [],
        'bishops': [],
        'knights': [],
        'casteling': []
    },

    'black':
        {
        'pawns': [],
        'rooks': [],
        'queens': [],
        'king': [],
        'bishops': [],
        'knights': [],
        'casteling': [],

    }
}
def append_O_to_other(that):
    if not that == 'r':
        board_struct['black']['rooks'].append(0)
    else:
        board_struct['black']['rooks'].append(1)
    if not that == 'n':
        board_struct["black"]["knights"].append(0)
    else:
        board_struct["black"]["knights"].append(1)
    if not that == 'b':
        board_struct["black"]["bishops"].append(0)
    else:
        board_struct["black"]["bishops"].append(1)
    if not that == 'q':
        board_struct["black"]["queens"].append(0)
    else:
        board_struct["black"]["queens"].append(1)
    if not that == 'k':
        board_struct["black"]["king"].append(0)
    else:
        board_struct["black"]["king"].append(1)
    if not that == 'p':
        board_struct["black"]["pawns"].append(0)
    else:
        board_struct["black"]["pawns"].append(0)


    if not that == 'R':
        board_struct['white']['rooks'].append(0)
    else:
        board_struct['white']['rooks'].append(1)
    if not that == 'N':
        board_struct["white"]["knights"].append(0)
    else:
        board_struct["white"]["knights"].append(1)
    if not that == 'B':
        board_struct["white"]["bishops"].append(0)
    else:
        board_struct["white"]["bishops"].append(1)
    if not that == 'Q':
        board_struct["white"]["queens"].append(0)
    else:
        board_struct["white"]["queens"].append(1)
    if not that == 'K':
        board_struct["white"]["king"].append(0)
    else:
        board_struct["white"]["king"].append(1)
    if not that == 'P':
        board_struct["white"]["pawns"].append(0)
    else:
        board_struct["white"]["pawns"].append(0)
def main(fen):

    on_board = True
    on_move = False
    on_castle = False
    space_count = 0



    for c in fen:
        is_lower = c.islower()
        if c == " ":
            on_board = False
            space_count += 1
        if space_count == 2:
            on_castle = True
            on_move = False

        if on_board:

            match c:










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

    },
    'en_pasant': ''
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



def distance_top(distance,row_index):

    if row_index >= distance:
        return True
    else:
        return

def distance_right(distance,colum_index):
    if 8 - colum_index >= distance:
        return True
    else:
        return False
def distance_bottom(distance,row_index):
    if 8 - row_index >= distance:
        return True
    else:
        return False
def distance_left(distance,row_index):
    if row_index >= distance:
        return False
    else:
        return True



def knight_movments(board_index):

    on_top_edge = top_edge(board_index)
    on_down_edge = down_edge(board_index)
    on_left_edge = left_edge(board_index)
    on_right_edge = right_edge(board_index)

    count = 0
    row_index = 0
    for i in range(0,64,8):
        if board_index >= i:
            row_index = count
            break
        count += 1

    on_row_index = board_index - (row_index * 8 - 1)

    directions = ['top','right','bottom','left']
    for direction in directions:

        for secondary_direction in secondary_directions:





def check_for_piece(pieces,white,index) -> bool: # usles ...
    Bools = []
    for piece in pieces:
        if white:
            if board_struct['white'][piece][index] == piece:
                Bools.append(True)
            else:
                Bools.append(False)
        else:
            if board_struct['black'][piece][index] == piece:
                Bools.append(True)
            else:
                Bools.append(False)
    return any(Bools)
def check_for_any(index,board=board_struct) -> list[str,str] or str:# returns the piece that is on the given index

    for outer_key in board_struct.keys():
        if key == 'en_pasant':
            continue
        for key in board_struct[outer_key].keys():
            if key == 'casteling':
                continue
            if key[index] == 1:
                return [key, outer_key]
    return 'no piece' # in the case that the index is empty on all ac


def rook_movments(board_index,function,color):
    not_on_edge = True
    move_index = board_index
    possibel_moves = []
    all_moves = []
    while not_on_edge:  # RIGHT →

        not_on_edge = not right_edge(move_index)
        if not_on_edge:
            move_index += 1
            possibel_moves.append(move_index)
            function()
            # TODO add check_index() function and action

    not_on_edge = True
    all_moves.append(possibel_moves)
    possibel_moves = []
    move_index = board_index


    while not_on_edge:  # LEFT ←

        not_on_edge = not left_edge(move_index)
        if not_on_edge:
            move_index -= 1
            possibel_moves.append(move_index)
    all_moves.append(possibel_moves)
    possibel_moves = []
    not_on_edge = True
    move_index = board_index  # reset

    while not_on_edge:  # TOP ↑

        not_on_edge = not top_edge(move_index)
        if not top_edge(move_index):
            move_index -= 8
            possibel_moves.append(move_index)
    all_moves.append(possibel_moves)
    possibel_moves = []
    not_on_edge = True
    move_index = board_index

    while not_on_edge:  # DOWN ↓

        not_on_edge = not down_edge(move_index)
        if not down_edge(move_index):
            move_index += 8
            possibel_moves.append(move_index)
        all_moves.append(possibel_moves)
        possibel_moves = []
    return all_moves


def bishop_movments(board_index):
    not_on_edge = True
    move_index = board_index
    possibel_moves = []
    all_moves = []
    while not_on_edge:  # RIGHT UP →

        not_on_edge = not (right_edge(move_index) or top_edge(move_index))
        if not_on_edge:
            move_index -= 7
            possibel_moves.append(move_index)
    all_moves.append(possibel_moves)
    possibel_moves = []
    not_on_edge = True
    move_index = board_index

    while not_on_edge:  # LEFT UP←

        not_on_edge = not (left_edge(move_index) or top_edge(move_index))
        if not_on_edge:
            move_index -= 9
            possibel_moves.append(move_index)
    all_moves.append(possibel_moves)
    possibel_moves = []
    not_on_edge = True
    move_index = board_index  # reset

    while not_on_edge:  # Down left ↓

        not_on_edge = not (down_edge(move_index) or left_edge(move_index))

        if not_on_edge:
            move_index += 7
            possibel_moves.append(move_index)

    all_moves.append(possibel_moves)
    possibel_moves = []
    not_on_edge = True
    move_index = board_index

    while not_on_edge:  # DOWN Right ↓

        not_on_edge = not (down_edge(move_index) or right_edge(move_index))
        if not_on_edge:
            move_index += 9
            possibel_moves.append(move_index)
    all_moves.append(possibel_moves)
    possibel_moves = []
    return all_moves




def is_check(board,white: bool) -> bool:
    if white:
        color = "white"
    else:
        color = "black"
    king_index = board[color]['king'].index()
    all_rook_moves = rook_movments(king_index)
    check_pieces = ['rook','bishops','knight','pawn','queen']
    for direction in all_rook_moves:
        for index in direction:
            if check_for_piece('rook',(not white),index=index):
                return True
            elif check_for_piece(check_pieces,white, index):
                break

    all_bishop_moves = bishop_movments(king_index)
    for direction in all_bishop_moves:
        for index in direction:
            for index in direction:
                if check_for_piece('bishops', (not white), index=index):
                    return True
                elif check_for_piece(check_pieces, white, index):
                    break
















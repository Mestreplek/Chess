
board = []
row = []
for i in range(8):
    for j in range(8):

        if j == 4 and i == 1:
            row.append(1)
        else:
            row.append(0)

    board.append(row)
    row = []
possible_movments = []



def rock_y_move(move_row_index,in_row_index,up_down):


    if move_row_index == 8 or move_row_index == -1:
        return 'break'

    move_square = board[move_row_index][in_row_index]

    if move_square == 1:

        return 'break'
    else:
        possible_movments.append(move_row_index, in_row_index)
def rook_move(board):

    in_row_index = 0
    row_index = 0
    for row in board:

        for square in row: # goes trhoug board to find pieces to move

            if square == 1:
                move_row_index += 1
                # top movment of rook
                move_row_index = row_index[:]
                for i in range(8):

                    if rock_y_move(move_row_index,in_row_index) == 'break':
                        break














            in_row_index += 1 # index in row

        in_row_index = 0 # reset when new row

    row_index += 1
print(board)


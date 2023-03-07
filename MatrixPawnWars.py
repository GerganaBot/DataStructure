# A chessboard has 8 rows and 8 columns. Rows, also called ranks, are marked from number 1 to 8, and columns are marked
# from A to H. We have a total of 64 squares. Each square is represented by a combination of letters and a number (a1, b1, c1, etc.).
# In this problem colors of the board will be ignored.
# We will play the game with two pawns, white (w) and black (b), where they can:
# · Only move forward in a straight line:
# § White (w) moves from the 1st rank to the 8th rank direction.
# § Black (b) moves from 8th rank to the 1st rank direction.
# · Can move only 1 square at a time.
# · Can capture another pawn in from of them only diagonally:
# When a pawn reaches the last rank (for the white one - this is the 8th rank, and for the black one - this is the 1st rank),
# can be promoted to a queen.
# Two pawns (w and b) will be placed on two random squares of the bord. The first move is always made by the white pawn (w),
# then black moves (b), then white (w) again, and so on.
# Some rules apply when moving paws:
# · If the two pawns interact diagonally, the player, in turn, must capture the opponent's pawn. When a pawn captures another pawn,
# the game is over.
# · If no capture is possible, the pawns keep on moving until one of them reaches the last rank.
# Input
# · On 8 lines, you will receive each row with its 8 columns, each element separated by a single space:
# o Empty positions are marked with "-".
# o White pawn is marked with "w"
# o Black pawn is marked with "b"
# Output
# Print either one of the following:
# · If a pawn captures the other, print:
# o "Game over! {White/Black} win, capture on {square}."
# · If a pawn reaches the last rank, print:
# o "Game over! {White/Black} pawn is promoted to a queen at {square}."
# Constraints
# · The input will always be valid.
# · The matrix will always be 8x8.
# · There will be no case where two pawns are placed on the same square.
# · There will be no case where two pawns are placed on the same column.
# · There will be no case where black/white will be placed on the last rank.

def find_player_position(matrix, player):
    for (row_index, row) in enumerate(matrix):
        if player in row:
            return (row_index, row.index(player))
    return (None, None)


def get_chess_position(row, column):
    row_names = [8, 7, 6, 5, 4, 3, 2, 1]
    column_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    return row_names[row], column_names[column]


ROWS_COUNT = 8
COLUMNS_COUNT = 8

matrix = [input().split(' ') for _ in range(ROWS_COUNT)]

current_player = 'w'
other_player = 'b'

current_player_position = find_player_position(matrix, 'w')
other_player_position = find_player_position(matrix, 'b')

current_delta = -1
other_delta = +1

is_capture = False
is_queen = False

while not is_queen and not is_capture:
    (current_player_row, current_player_column) = current_player_position
    (other_player_row, other_player_column) = other_player_position
    
    current_player_row += current_delta
    current_player_position = (current_player_row, current_player_column)
    
    if current_player_row == other_player_row and abs(current_player_column - other_player_column) == 1:
        is_capture = True
        current_player_position = (current_player_row, other_player_column)
    elif current_player_row in (0, ROWS_COUNT - 1):
        is_queen = True
    else:
        current_player_position, other_player_position = other_player_position, current_player_position
        current_delta, other_delta = other_delta, current_delta
        current_player, other_player = other_player, current_player

player = 'White' if current_player == 'w' else 'Black'
(row_name, column_name) = get_chess_position(*current_player_position)
position_name = f'{column_name}{row_name}'
        
if is_capture:
    print(f'Game over! {player} win, capture on {position_name}.')
    
if is_queen:
    print(f'Game over! {player} pawn is promoted to a queen at {position_name}.')



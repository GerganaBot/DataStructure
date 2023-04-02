def find_player_coordinates(row, col, matrix):
    for r in range(row):
        for c in range(col):
            if matrix[r][c] == "B":
                return [r, c]


def player_next_position(player_row, player_col, current_matrix):
    if 0 <= player_row < len(current_matrix) and 0 <= player_col < len(current_matrix[0]):
        next_position = current_matrix[player_row][player_col]
        if next_position == "O":
            return False
        elif next_position == "-":
            return [player_row, player_col], current_matrix, 0
        elif next_position == "P":
            current_matrix[player_row][player_col] = "-"
            return [player_row, player_col], current_matrix, 1


n, m = map(int, input().split())

matrix = []
for _ in range(n):
    matrix.append(input().split())


player_coordinates = find_player_coordinates(n, m, matrix)
matrix[player_coordinates[0]][player_coordinates[1]] = "-"
result = False
touched_opponents = 0
moves_made = 0

while True:
    if touched_opponents == 3:
        break

    command = input()
    if command == 'Finish':
        break

    if command == 'up':
        result = player_next_position(player_coordinates[0] - 1, player_coordinates[1], matrix)
    elif command == 'down':
        result = player_next_position(player_coordinates[0] + 1, player_coordinates[1], matrix)
    elif command == 'left':
        result = player_next_position(player_coordinates[0], player_coordinates[1] - 1, matrix)
    elif command == 'right':
        result = player_next_position(player_coordinates[0], player_coordinates[1] + 1, matrix)

    if result:
        player_coordinates, matrix, touches = result
        touched_opponents += touches
        moves_made += 1

print("Game over!")
print(f"Touched opponents: {touched_opponents} Moves made: {moves_made}")





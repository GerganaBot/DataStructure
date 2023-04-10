# First, you will be given the names "Tom" and "Jerry", separated by a comma and a space ", ". The order in which they
# are received determines the order in which they will take turns. The first player starts first.
# Next, you will be given a matrix with 6 rows and 6 columns representing the maze board. It consists of:
# •	Only one Exit - marked with the "E" letter
# •	Trap (one, many, or none) - marked with the "T" letter
# •	Wall (one, many, or none) - marked with the "W" letter
# •	Empty positions will be marked with "."
# In the beginning, Tom and Jerry are outside the board. On each line, after the matrix is given, you will be receiving
# coordinates for each of the players. They will be taking turns and stepping on different positions on the board until
# one of them find the Exit or falls into a Trap. Here are the rules:
# •	If a player hits the letter "E", he escapes the maze and wins the game.
# o	Print "{player} found the Exit and wins the game!" and end the program.
# •	If the letter "T" is hit, the player falls into a Trap, the game ends, and his opponent wins automatically.
# o	Print "{player} is out of the game! The winner is {winner}." and end the program.
# •	If the letter "W" is hit, the player hits a wall, and he needs to rest. The player's next move is ignored.
# o	Print "{player} hits a wall and needs to rest."
# •	If a player steps on an empty position ".", nothing happens.
# •	Both players can step in the same position at the same time.

player_one, player_two = input().split(', ')

matrix = []

for _ in range(6):
    matrix.append(input().split())

player_one_needs_rest = False
player_two_needs_rest = False

while True:
    player_one_coordinates = input()
    if not player_one_needs_rest:
        row, column = map(int, player_one_coordinates.strip('(').strip(')').split(', '))
        position = matrix[row][column]
        if position == 'E':
            print(f'{player_one} found the Exit and wins the game!')
            break
        if position == 'T':
            print(f'{player_one} is out of the game! The winner is the {player_two}.')
            break
        if position == 'W':
            print(f'{player_one} hits a wall and needs to rest.')
            player_one_needs_rest = True
    else:
        player_one_needs_rest = False

    player_two_coordinates = input()
    if not player_two_needs_rest:
        row, column = map(int, player_two_coordinates.strip('(').strip(')').split(', '))
        position = matrix[row][column]
        if position == 'E':
            print(f'{player_two} found the Exit and wins the game!')
            break
        if position == 'T':
            print(f'{player_two} is out of the game! The winner is the {player_one}')
            break
        if position == 'W':
            print(f'{player_two} hits a wall and needs to rest.')
            player_two_needs_rest = True
    else:
        player_two_needs_rest = False





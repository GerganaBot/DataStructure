# You will be given an integer n for the size of the battlefield (square shape). On the next n lines, you will receive
# the rows of the battlefield. The submarine will start at a random position, marked with the letter 'S'. The submarine
# surveys the surrounding area through its periscope, so it has to climb up to periscope depth, where it might run across
# naval mines.
# When the submarine receives direction, it goes deep and moves one position toward the given direction. On each turn,
# you will be guiding the submarine and giving it the direction, in which it should move. The commands will be "up", "down",
# "left" and "right".
# When a new position is reached,  the submarine climbs up to periscope depth to search for a cruiser:
# •	If a position with '-' (dash) is reached, it means that the field is empty and the submarine awaits its next direction.
# •	If it runs across a naval mine ('*'), the submarine takes serious damage. When a mine is blown, the position of the
# mine will be marked with '-' (dash). U-9 can withstand two hits from naval mines.  The third time the submarine is hit
# by a mine, it disappears and the mission is failed. The battle is over and the following message should be printed on
# the Console: "Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!"
# •	If a battle cruiser is reached ('C'), the submarine destroys it and the position of the destroyed cruiser will be
# marked with '-' (dash).
# •	If this is the last (third) battle cruiser on the battlefield, the battle is over and the following message should be
# printed on the Console: "Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!"
# The program will end when the battle is over (All battle cruisers are destroyed or the submarine hits mines three times).

battlefield_size = int(input())

matrix = []
cruisers = []
hits_counter = 0
position = [0, 0]

for i in range(battlefield_size):
    row = list(input())
    matrix.append(row)
    if 'S' in row:
        position = [i, row.index('S')]
    if 'C' in row:
        for c_index in range(len(row)):
            if row[c_index] == 'C':
                cruisers.append([i, c_index])

matrix[position[0]][position[1]] = '-'
while True:
    command = input()
    if command == 'left':
        position[1] -= 1
    elif command == 'right':
        position[1] += 1
    elif command == 'up':
        position[0] -= 1
    elif command == 'down':
        position[0] += 1
    if matrix[position[0]][position[1]] == '-':
        continue
    if matrix[position[0]][position[1]] == '*':
        hits_counter += 1
        matrix[position[0]][position[1]] = '-'
        if hits_counter == 3:
            print(f'Mission failed, U-9 disappeared! Last known coordinates {position}!')
            matrix[position[0]][position[1]] = 'S'
            break
    if matrix[position[0]][position[1]] == 'C':
        cruiser_position = [position[0], position[1]]
        cruisers.pop(cruisers.index(cruiser_position))
        matrix[position[0]][position[1]] = '-'
        if not cruisers:
            print(f'Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!')
            matrix[position[0]][position[1]] = 'S'
            break

for row in range(len(matrix)):
    print("".join(matrix[row]))

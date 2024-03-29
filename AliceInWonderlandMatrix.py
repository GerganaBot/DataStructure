﻿# Alice is going to the mad tea party, to see her friends. On the way to the party, she needs to collect bags of tea.
# You will be given an integer n for the size of the Wonderland territory with a square shape. On the following n lines,
# you will receive the rows of the territory:
# · Alice will be placed in a random position, marked with the letter "A".
# · On the territory, there will be bags of tea, represented as numbers. If Alice steps on a number position, she collects
# the tea bags and increases the quantity with the corresponding number.
# · There will always be one rabbit hole on the territory marked with the letter "R".
# · All of the empty positions will be marked with ".".
# After the field state, you will be given commands for Alice's movements. Move commands can be: "up", "down", "left" or "right".
# When Alice collects at least 10 bags of tea, she is ready to go to the tea party, and she does not need to continue collecting.
# Otherwise, if she steps on the rabbit hole or goes out of the territory, she can't return, and the program ends.
# In the end, the path she walked had to be marked with '*'.
# For more clarifications, see the examples below.
# Input
# · On the first line, you will be given the integer n – the size of the square matrix
# · On the following n lines - matrix representing the field (each position separated by a single space)
# · On each of the following lines, you will be given a move command
# Output
# · On the first line:
# o If Alice steps on the rabbit hole or she goes out of the territory, print:
# "Alice didn't make it to the tea party."
# o If she collected at least 10 bags of tea, print:
# "She did it! She went to the party."
# · On the following lines, print the matrix.
# Constraints
# · Alice will always either go outside the Wonderland or collect 10 bags of tea
# · All the commands will be valid
# · All of the given numbers will be valid integers in the range [0, 10]


def get_next_position(row, col, direction):
    if direction == 'up':
        return row - 1, col
    if direction == 'down':
        return row + 1, col
    if direction == 'left':
        return row, col - 1
    if direction == 'right':
        return row, col + 1


size = int(input())
matrix = []

alice_row = 0
alice_col = 0

for row in range(size):
    row_elements = input().split()
    for col in range(size):
       if row_elements[col] == 'A':
           alice_row = row
           alice_col = col
    matrix.append(row_elements)

tea_bags = 0
while tea_bags < 10:
    matrix[alice_row][alice_col] = '*'
    
    direction = input()
    next_row, next_col = get_next_position(alice_row, alice_col, direction)
    
    if next_row < 0 or next_col < 0 or next_row >= size or next_col >= size:
        break
        
    alice_row, alice_col = next_row, next_col
    
    if matrix[alice_row][alice_col] == '.' or matrix[alice_row][alice_col] == '*':
        continue
    
    if matrix[alice_row][alice_col] == 'R':
        break
        
    tea_bags += int(matrix[alice_row][alice_col])

matrix[alice_row][alice_col] = '*'

if tea_bags >= 10:
    print('She did it! She went to the party.')
else:
    print('Alice did not make it to the tea party.')
    
for row in matrix:
    print(*row, sep=' ')


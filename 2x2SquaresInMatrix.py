# Find the number of all 2x2 squares containing identical chars in a matrix. On the first line, you will receive the matrix's
# dimensions in the format "{rows} {columns}". On the following rows, you will receive characters separated by a single space.
# Print the number of all square matrices you have found.

rows, cols = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    matrix.append([x for x in input().split()])

square_matrices_num = 0
start_row = 0
start_col = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        if matrix[row][col] == matrix[row][col + 1] == matrix[row + 1][col] == matrix[row + 1][col + 1]:
            square_matrices_num += 1
            start_row = row
            start_col = col
            
print(square_matrices_num)



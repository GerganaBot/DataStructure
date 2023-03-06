# Write a program that reads a matrix from the console and prints the sum for each column on separate lines.
# On the first line, you will get matrix sizes in format "{rows}, {columns}". On the next rows, you will get elements for
# each column separated with a single space.

rows_count, columns_count = [int(x) for x in input().split(', ')]

matrix = []

for _ in range(rows_count):
    row = [int(x) for x in input().split()]
    matrix.append(row)
    
result = []

for column_index in range(columns_count):
    column_sum = 0
    for row_index in range(rows_count):
        column_sum += matrix[row_index][column_index]
    result.append(column_sum)
    
[print(x) for x in result]


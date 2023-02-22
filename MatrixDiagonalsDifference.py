# Write a program that finds the difference between the sums of the square matrix diagonals (absolute value).
# On the first line, you will receive an integer N - the size of a square matrix. The following N lines hold the values
# for each column - N numbers separated by a single space. Print the absolute difference between the primary and the secondary diagonal sums.

matrix_size = int(input())

matrix = []

for _ in range(matrix_size):
    matrix.append([int(x) for x in input().split()])

primary_diagonal = []
secondary_diagonal = []

for idx in range(matrix_size):
    primary_diagonal.append(matrix[idx][idx])
    secondary_diagonal.append(matrix[idx][- 1 - idx])

primary_sum = sum(primary_diagonal)
secondary_sum = sum(secondary_diagonal)

print(f'Primary diagonal: sum = {", ".join([str(x) for x in primary_diagonal])} = {sum(primary_diagonal)}')
print(f'Secondary diagonal: sum = {", ".join([str(x) for x in secondary_diagonal])} = {sum(secondary_diagonal)}')
print(f'Difference: |{primary_sum} - {secondary_sum}| = {abs(primary_sum - secondary_sum)}')



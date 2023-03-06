﻿# You will be given numbers separated by a space. Write a program that prints the number of occurrences of each number
# in the format "{number} - {count} times". The number must be formatted to the first decimal point.

numbers = tuple(map(float, input().split()))

nums_and_occurrences = {}

for num in numbers:
    if num not in nums_and_occurrences:
        nums_and_occurrences[num] = 0
    nums_and_occurrences[num] += 1

[print(f'{key} - {value} times') for key, value in nums_and_occurrences.items()]
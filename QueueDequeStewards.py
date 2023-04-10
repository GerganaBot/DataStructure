# You will be given a sequence of 6 seats - every seat is a mix of a number and a letter in the format "{number}{letter}".
# You will also be given two more sequences of numbers only.
# First, you have to take the first number of the first sequence and the last number of the second sequence. Next, take
# the sum of those two numbers and find its ASCII character.
# •	Compare each of the two taken numbers and the found character with the seats. If you find a match, the passenger is
# seated, and the seat is considered taken. Remove both numbers from their sequences.
# •	If there is no equality, the two numbers should be returned at the end of their sequences (first becomes last, last
# becomes first).
# •	If you match an already taken seat, you should just remove both numbers from their sequences.
# Each time you take numbers from the sequences and try to match them, you make one rotation. You should keep track of all
# rotations made.
# The program should end under the following circumstances:
# •	You have found 3 (three) seat matches
# •	You have made a total of 10 rotations


from collections import deque

seats = input().split(', ')
first_nums = deque(map(int, input().split(', ')))
second_nums = deque(map(int, input().split(', ')))

rotations = 0
taken_seats = []

while True:
    if rotations == 10:
        break
    if len(taken_seats) == 3:
        break
    first_number = first_nums.popleft()
    second_number = second_nums.pop()
    sum_of_nums = first_number + second_number
    ascii_char = chr(sum_of_nums)
    first_concatenation = str(first_number) + ascii_char
    second_concatenation = str(second_number) + ascii_char
    for seat in [first_concatenation, second_concatenation]:
        if seat in taken_seats:
            break
        if seat in seats:
            seats.remove(seat)
            taken_seats.append(seat)
            break
    else:
        first_nums.append(first_number)
        second_nums.appendleft(second_number)
    rotations += 1

print(f'Seat matches: {", ".join(taken_seats)}')
print(f'Rotations count: {rotations}')

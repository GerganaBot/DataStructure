# You will receive three integer numbers. Write a program that finds if their multiplication (the result) is negative, positive, or zero.
# Try to do this WITHOUT multiplying the 3 numbers.

first_int = int(input())
second_int = int(input())
third_int = int(input())


def multiplication_sign(first, second, third):
    ints_list = list()
    ints_list.extend([first, second, third])
    negatives = 0
    for el in ints_list:
        if el < 0:
            negatives += 1
        elif el == 0:
            return 'Zero'
    if negatives % 2 == 0:
        result = 'Positive'
    else:
        result = 'Negative'
    return result


print(multiplication_sign(first_int, second_int, third_int))
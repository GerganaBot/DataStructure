# You will receive a sequence of numbers (integers) separated by a single space. Separate the negative numbers from the positive.
# Find the total sum of the negatives and positives, and print the following:
# · On the first line, print the sum of the negatives
# · On the second line, print the sum of the positives
# · On the third line:
# o If the absolute negative number is larger than the positive number: "The negatives are stronger than the positives"
# o If the positive number is larger than the absolute negative number: "The positives are stronger than the negatives"
# Note: you will not receive any zeroes in the input.

def find_positive_and_negative_sums(*args):
    positive_sum = 0
    negative_sum = 0
    
    for element in args:
        if element > 0:
            positive_sum += element
        else:
            negative_sum += element

    return positive_sum, negative_sum


nums = [int(x) for x in input().split()]

positive_sum, negative_sum = find_positive_and_negative_sums(*nums)

print(negative_sum)
print(positive_sum)

if abs(negative_sum) > positive_sum:
    print('The negatives are stronger than the positives')
else:
    print('The positives are stronger than the negatives')
    
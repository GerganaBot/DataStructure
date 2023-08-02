# Write a function that receives a string and a counter n. The function should return a new string – the result of repeating
# the old string n times. Print the result of the function. Try using lambda

word = input()
counter = int(input())

repeat_string = lambda a, b: a * b
result = repeat_string(word, counter)

print(result)

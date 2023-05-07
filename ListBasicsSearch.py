# On the first line, you will receive a number n. On the second line, you will receive a word. On the following n lines,
# you will be given some strings. You should add them to a list and print them. After that, you should filter out only
# the strings that include the given word and print that list too.

n = int(input())
word = input()
strings = []

for i in range(n):
    current_str = input()
    strings.append(current_str)

print(strings)

for i in range(len(strings) - 1, -1, -1):
    element = strings[i]
    if word not in element:
        strings.remove(element)

print(strings)


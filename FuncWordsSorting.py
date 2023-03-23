# Write a function words_sorting which receives a different number of words.
# Create a dictionary, which will have as keys the words that the function received. For each key, create a value that is
# the sum of all ASCII values of that key.
# Then, sort the dictionary:
# · By values in descending order, if the sum of all values of the dictionary is odd
# · By keys in ascending order, if the sum of all values of the dictionary is even
# Input
# · There will be no input, just any number of words passed to your function
# Output
# · The function should return a string in the format "{key} - {value}" for each key and value on a separate lines
# Constraints:
# · There will be no case with capital letters.
# · There will be no case with a string consisting of other than letters.

def words_sorting(*args):
    def calculate_word_value(word):
        return sum(ord(x) for x in word)

    words_dict = {word: calculate_word_value(word) for word in args}

    total_words_value = sum(words_dict.values())
    if total_words_value % 2 == 0:
        result = sorted(words_dict.items())
    else:
        result = sorted(words_dict.items(), key=lambda x: x[1], reverse=True)

    return '\n'.join(f'{word} - {count}' for (word, count) in result)

print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
    ))
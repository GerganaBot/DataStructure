# Having the following list of words:
# luxuriant, silly, dizzy, frightening, blink, silly, enjoy, suspend, blink, reward, blink, fact, debt, marble, blink, yak, frightening, suspend, debt
#
# Generate horizontal histogram that represents how often each word appears in the collection above.
# Each line of the histogram must be in the following format:
# word |*
# where the number of asterisks(*) is equal to the number of occurrences of the word.
#
# Example:
# the word "horse" appears 6 times in the list, then its line in the histogram must look like this:
# horse |******

words_list = ['luxuriant', 'silly', 'dizzy', 'frightening', 'blink', 'silly', 'enjoy', 'suspend', 'blink', 'reward', 'blink', 'fact', 'debt', 'marble', 'blink', 'yak', 'frightening', 'suspend', 'debt']
words_dict = dict()
for word in words_list:
    if word not in words_dict:
        words_dict[word] = '*'
    else:
        words_dict[word] += '*'

sorted_list = sorted(words_dict.items(), key=lambda x: (-len(x[1]), x[0]))
for word in sorted_list:
    print(f'{word[0]} |{word[1]}')

# Write a program that rounds all the given numbers, separated by a single space, and prints the result as a list.
# Use round().

string_of_floats = input().split(' ')

def rounding(base_list):
    final_list = list()
    for n in base_list:
        final_n = round(float(n))
        final_list.append(final_n)
    return final_list


print(rounding(string_of_floats))
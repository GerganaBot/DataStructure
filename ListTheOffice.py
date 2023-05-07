# You will receive two lines of input:
# · a list of employees' happiness as a string of numbers separated by a single space
# · a happiness improvement factor (single number).
# Your task is to find out if the employees are generally happy in their office.
# First, multiply each employee's happiness by the factor.
# Then, print one of the following lines:
# · If half or more of the employees have happiness greater than or equal to the average:
# "Score: {happy_count}/{total_count}. Employees are happy!"
# · Otherwise:
# "Score: {happy_count}/{total_count}. Employees are not happy!"

employees_happiness = input().split(' ')
happiness_factor = int(input())

employees_happiness = list(map(lambda x: int(x) * happiness_factor, employees_happiness))
filtered = list(filter(lambda x: x >= sum(employees_happiness) / len(employees_happiness), employees_happiness))

if len(filtered) >= len(employees_happiness) / 2:
    print(f'Score: {len(filtered)}/{len(employees_happiness)}. Employees are happy.')
else:
    print(f'Score: {len(filtered)}/{len(employees_happiness)}. Employees are not happy.')

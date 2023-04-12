#You will be given two sequences of integers. The first one represents the time it takes a programmer to complete a single task.
# The second one represents the number of tasks you’ve given to your programmers.
# Your task is to count how many rubber ducks of each type you’ve given to your programmers.
# While you have values in the sequences, you need to start from the first value of the programmers time's sequence and
# multiply them by the last value of the tasks' sequence:
# •	If the calculated time is between any of the time ranges below, you give the corresponding ducky and remove the programmer
# time's value and the tasks' value.
# •	If the calculated time goes above the highest range, decrease the number of the tasks' value by 2. Then, move the programmer
# time's value to the end of its sequence, and continue with the next operation.
# Rubber Ducky type	Time needed to earn it
# Darth Vader Ducky	0 - 60
# Thor Ducky	61 – 120
# Big Blue Rubber Ducky	121 - 180
# Small Yellow Rubber Ducky	181 - 240
# Your task is considered done when the sequences are empty.

from collections import deque

time_for_task = deque(map(int, input().split()))
number_of_tasks = list(map(int, input().split()))

darth_vader_ducky = 0
thor_ducky = 0
big_blue_rubber_ducky = 0
small_yellow_rubber_ducky = 0

while time_for_task and number_of_tasks:
    time_value = time_for_task.popleft()
    task_value = number_of_tasks.pop()
    result = time_value * task_value
    if 0 <= result <= 60:
        darth_vader_ducky += 1
    elif 61 <= result <= 120:
        thor_ducky += 1
    elif 121 <= result <= 180:
        big_blue_rubber_ducky += 1
    elif 181 <= result <= 240:
        small_yellow_rubber_ducky += 1
    elif result > 240:
        task_value -= 2
        number_of_tasks.append(task_value)
        time_for_task.append(time_value)


print('Congratulations, all tasks have been completed! Rubber ducks rewarded: ')
print(f'Darth Vader Ducky: {darth_vader_ducky}')
print(f'Thor Ducky: {thor_ducky}')
print(f'Big Blue Rubber Ducky: {big_blue_rubber_ducky}')
print(f'Small Yellow Rubber Ducky: {small_yellow_rubber_ducky}')

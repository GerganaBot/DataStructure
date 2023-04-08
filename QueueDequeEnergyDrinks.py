# Your friend Stamat is working on a new AI program. Like every irresponsible teenager, he programs all night and, of
# course, drinks a lot of energy drinks. Stamat's friends are concerned about him and want you to create a program that
# tells him when to stop the energy drinks and start drinking water.
# On the first line, you will receive a sequence of numbers representing milligrams of caffeinе. On the second line, you
# will receive another sequence of numbers representing energy drinks. It is important to know that the maximum caffeine
# Stamat can have for the night is 300 milligrams, and his initial is always 0.
# To calculate the caffeine in the drink take the last milligrams of caffeinе and the first energy drink, and multiply them.
# Then, compare the result with the caffeine Stamat drank:
# •	If the sum of the caffeine in the drink and the caffeine that Stamat drank doesn't exceed 300 milligrams, remove both
# the milligrams of caffeinе and the drink from their sequences. Also, add the caffeine to Stamat's total caffeine.
# •	If Stamat is about to exceed his maximum caffeine per night, do not add the caffeine to Stamat’s total caffeine.
# Remove the milligrams of caffeinе and move the drink to the end of the sequence. Also, reduce the current caffeine that
# Stamat has taken by 30 (Note: Stamat's caffeine cannot go below 0).
# Stop calculating when you are out of drinks or milligrams of caffeine.


from collections import deque

caffeine_milligrams = list(map(int, input().split(',')))
energy_drinks = deque(map(int, input().split(',')))

total_caffeine = 0
max_caffeine = 300

while caffeine_milligrams and energy_drinks:
    current_caffeine = caffeine_milligrams.pop()
    current_drink = energy_drinks.popleft()
    result = current_caffeine * current_drink
    if result + total_caffeine <= max_caffeine:
        total_caffeine += result
    else:
        energy_drinks.append(current_drink)
        total_caffeine -= 30
        if total_caffeine < 0:
            total_caffeine = 0


if energy_drinks:
    print(f"Drinks left: {', '.join(map(str, energy_drinks))}")
else:
    print(f'At least Stamat wasn\'t exceeding the maximum caffeine.')

print(f'Stamat is going to sleep with {total_caffeine} mg caffeine.')



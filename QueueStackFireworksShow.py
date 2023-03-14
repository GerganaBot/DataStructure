# Maria wants to make a firework show for the wedding of her best friend.
# We should help her to make the perfect firework show.
# First, you will be given a sequence of integers representing firework effects. Afterwards you will be given another
# sequence of integers representing explosive power.
# You need to start from the first firework effect and try to mix it with the last explosive power. If the sum of their
# values is:
# divisible by 3, but it is not divisible by 5 – create Palm firework and remove both materials
# divisible by 5, but it is not divisible by 3 – create Willow firework and remove both materials
# divisible by both 3 and 5 – create Crossette firework and remove both materials
# Otherwise, decrease the value of the firework effect by 1 and move it at the end of the sequence. Then, try to mix the
# same explosive power with the next firework effect.
# If any value is equal to or below 0, you should remove it from the sequence before trying to mix it with the other.
# When you have successfully prepared enough fireworks for the show or you have no more firework punches or explosive power,
# you need to stop mixing.
# To make the perfect firework show, Maria needs 3 of each of the firework types.
# Input
# On the first line, you will receive the integers representing the firework effects, separated by ", ".
# On the second line, you will receive the integers representing the explosive power, separated by ", ".
# Output
# On the first line, print:
# if Maria successfully prepared the firework show: "Congrats! You made the perfect firework show!"
# if Maria failed to prepare it: "Sorry. You can't make the perfect firework show."
# On the second line, print all firework effects left if there are any:
# "Firework Effects left: {effect1}, {effect2}, (…)"
# On the third line, print all explosive fillings left if there are any:
# " Explosive Power left: {filling1}, {filling2}, (…)"
# Then, you need to print all fireworks and the amount you have of them:
# "Palm Fireworks: {count}"
# "Willow Fireworks: {count}"
# "Crossette Fireworks: {count}"


from collections import deque


def mix_effect_and_power(effects, powers):
     current_effect = effects.popleft() 
     current_power = powers.pop()

     while effects and powers and current_effect <= 0 or current_power <= 0:
         if current_effect <= 0:
             current_effect = effects.popleft()
         if current_power <= 0:
             current_power = powers.pop()

     result = current_effect + current_power
     if result <= 0:
         powers.append(current_power)

     while result % 5 != 0 and result % 3 != 0 and result > 0:
         current_effect -= 1
         effects.append(current_effect)
         new_current_effect = effects.popleft()
         result = new_current_effect + current_power
     
     return result


firework_effects_input = [int(x) for x in input().split(', ')]
explosive_power = [int(x) for x in input().split(', ')]

firework_effects = deque(firework_effects_input)

palm_fireworks = 0
willow_fireworks = 0
crossette_fireworks = 0

while firework_effects and explosive_power:
    result = mix_effect_and_power(firework_effects, explosive_power)
    if result % 3 == 0 and result % 5 != 0:
        palm_fireworks += 1
        continue
    elif result % 5 == 0 and result % 3 != 0:
        willow_fireworks += 1
        continue
    elif result % 5 == 0 and result % 3 == 0:
        crossette_fireworks += 1
    if palm_fireworks == 3 and willow_fireworks == 3 and crossette_fireworks == 3:
        break
    if result == 0:
        break

if palm_fireworks >= 3 and willow_fireworks >= 3 and crossette_fireworks >= 3:
    print('Congrats! You made the perfect firework show!')
else:
    print('Sorry. You can\'t make the perfect firework show.')

formatted_left_effects = ', '.join(str(x) for x in firework_effects)
formatted_left_powers = ', '.join(str(x) for x in explosive_power)

if firework_effects:
    print(f'Firework Effects left: {formatted_left_effects}')
if explosive_power:
    print(f'Explosive Power left: {formatted_left_powers}')


print(f'Palm Fireworks: {palm_fireworks}')
print(f'Willow Fireworks: {willow_fireworks}')
print(f'Crossette Fireworks: {crossette_fireworks}')

        
    

  









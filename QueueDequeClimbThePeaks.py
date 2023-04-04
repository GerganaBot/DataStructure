from collections import deque


food_portions = list(map(int, input().split(',')))
stamina = deque(map(int, input().split(',')))

day = 1
conquered_peaks = []
target_peaks = deque([
    ("Vihren", 80),
    ("Kutelo", 90),
    ("Banski Suhodol", 100),
    ("Polezhan", 60),
    ("Kamenitza", 70)
])

while True:
    if len(conquered_peaks) == 5:
        print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
        break
    if day > 7 or not food_portions or not stamina:
        print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
        break
    current_food = food_portions.pop()
    current_stamina = stamina.popleft()
    result = current_food + current_stamina
    index = 0
    next_peak = target_peaks.popleft()
    if result >= next_peak[1]:
        conquered_peaks.append(next_peak[0])
        day += 1
    else:
        target_peaks.appendleft(next_peak)
        day += 1

if conquered_peaks:
    print(f'Conquered peaks:')
    for peak in conquered_peaks:
        print(peak)

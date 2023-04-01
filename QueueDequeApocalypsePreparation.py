from collections import deque

textiles = deque(map(int, input().split()))
medicines = list(map(int, input().split()))

items = {"Patch": 0, "Bandage": 0, "MedKit": 0}

while True:
    if not textiles and not medicines:
        print("Textiles and medicaments are both empty.")
        break
    if not textiles:
        print("Textiles are empty.")
        break
    if not medicines:
        print("Medicaments are empty.")
        break
    first_textile = textiles.popleft()
    last_medicament = medicines.pop()
    summed_items = first_textile + last_medicament
    if summed_items == 30:
        items["Patch"] += 1
    elif summed_items == 40:
        items["Bandage"] += 1
    elif summed_items == 100:
        items["MedKit"] += 1
    elif summed_items > 100:
        items["MedKit"] += 1
        summed_items -= 100
        medicines[-1] += summed_items
    else:
        last_medicament += 10
        medicines.append(last_medicament)

sorted_items = sorted(items.items(), key=lambda x: (-x[1], x[0]))
for item in sorted_items:
    if int(item[1]) > 0:
        print(f"{item[0]} - {item[1]}")

if medicines:
    medicines.reverse()
    print(f"Medicaments left: {', '.join(map(str, medicines))}")
if textiles:
    print(f"Textiles left: {', '.join(map(str, textiles))}")

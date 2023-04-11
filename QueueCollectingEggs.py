from collections import deque

eggs = deque(int(x) for x in input().split(', '))
papers = deque(int(x) for x in input().split(', '))

box = 50
total_boxes = 0

while eggs and papers:
    current_egg = eggs.popleft()
    current_paper = papers.pop()
    if current_egg <= 0:
        papers.append(current_paper)
    elif current_egg == 13:
        first_paper = papers.popleft()
        papers.append(first_paper)
        papers.appendleft(current_paper)
    else:
        if current_paper + current_egg <= box:
            total_boxes += 1
        else:
            continue

if total_boxes > 0:
    print(f'Great! You filled {total_boxes} boxes.')
else:
    print(f'You couldn\'t fill any boxes!')
if papers:
    print(f'Pieces of paper left: {", ".join(str(el) for el in papers)}')
if eggs:
    print(f'Eggs left: {", ".join(str(el) for el in eggs)}')


# You will be given two sequences of integers representing bowls of ramen and customers. Your task is to find out if you
# can serve all the customers.
# Start by taking the last bowl of ramen and the first customer. Try to serve every customer with ramen until we have no
# more ramen or customers left:
# •	Each time the value of the ramen is equal to the value of the customer, remove them both and continue with the next
# bowl of ramen and the next customer.
# •	Each time the value of the ramen is bigger than the value of the customer, decrease the value of that ramen with the
# value of that customer and remove the customer. Then try to match the same bowl of ramen (which has been decreased) with
# the next customer.
# •	Each time the customer's value is bigger than the value of the ramen bowl, decrease the value of the customer with the
# value of the ramen bowl and remove the bowl. Then try to match the same customer (which has been decreased) with the next
# bowl of ramen.

from collections import deque

bowls = deque(map(int, input().split(', ')))
customers = deque(map(int, input().split(', ')))

while bowls and customers:
    last_bowl = bowls.pop()
    first_customer = customers.popleft()
    if first_customer > last_bowl:
        first_customer -= last_bowl
        customers.appendleft(first_customer)
    elif first_customer < last_bowl:
        last_bowl -= first_customer
        bowls.append(last_bowl)
    elif first_customer == last_bowl:
        bowls.pop()
        customers.popleft()

if len(customers) == 0:
    print(f'Great job! You served all the customers.')
elif len(bowls) == 0:
    print(f'Out of ramen! You didn\'t manage to serve all customers.')
if bowls:
    print(f'Bowls of ramen left: {", ".join(map(str, bowls))}')
if customers:
    print(f'Customers left: {", ".join(map(str, customers))}')

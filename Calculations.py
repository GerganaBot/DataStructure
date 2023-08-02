# Create a function that receives three parameters, calculates a result depending on the given operator, and returns it.
# Print the result of the function.
# The input comes as three parameters – an operator as a string and two integer numbers. The operator can be one of the
# following: "multiply", "divide", "add", "subtract".

def calculate(first_int, second_int, operator):
    result = 0
    if operator == 'multiply':
        result = first_int * second_int
    elif operator == 'divide':
        result = int(first_int / second_int)
    elif operator == 'add':
        result = first_int + second_int
    elif operator == 'subtract':
        result = first_int - second_int
    return result


first_int = int(input())
second_int = int(input())
operator = input()

print(calculate(first_int, second_int, operator))
def operate(operation, *args):
    def add(*args):
        return sum(x for x in args)

    def subtract(x, *args):
        return x - sum(-y for y in args[1:])

    def multiply(*args):
        result = 1
        for value in args:
            result *= value
        return result

    def divide(x, *args):
        result = x
        for value in args[1:]:
            result /= value
        return result
    
    if operation == '+':
        return add(*args)
    elif operation == '-':
        return subtract(*args)
    elif operation == '*':
        return multiply(*args)
    elif operation == '/':
        return divide(*args)


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))


# Create a function called rectangle(). It must have two parameters - length and width.
# First, you need to check if the given arguments are integers:
# · If one/ both of them is/ are NOT an integer/s, return the string "Enter valid values!"
# Create two inner functions:
# · area() - returns the area of the rectangle with the given length and width
# · perimeter() - returns the perimeter of the rectangle with the given length and width
# In the end, the rectangle function should return a string containing the area and the perimeter of a rectangle in the following format:
# "Rectangle area: {ract_area}
# Rectangle perimeter: {rect_perim}"

def rectangle(length, width):
    if not isinstance(length, int) or not isinstance(width, int):
        return f'Enter valid values!'

    def area(a, b):
        return a * b

    def perimeter(a, b):
        return 2*(a + b)

    return f'Rectangle area: {area(length, width)}\nRectangle perimeter: {perimeter(length, width)}'


print(rectangle('2', 10))
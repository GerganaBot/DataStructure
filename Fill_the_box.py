# Write a function called fill_the_box that receives a different number of arguments representing:
# · the height of a box
# · the length of a box
# · the width of a box
# · n-times a different number of cubes with exact size 1 x 1 x 1
# · a string "Finish"
# Your task is to fill the box with the given cubes until the current argument equals "Finish".
# Note: Submit only the function in the judge system
# Input
# · There will be no input. Just parameters passed to your function.
# Output
# The function should return a string in the following format:
# · If, at the end, there is free space left in the box, print:
# o "There is free space in the box. You could put {free space in cubes} more cubes."
# · If there is no free space in the box, print:
# o "No more free space! You have {cubes left} more cubes."

def fill_the_box(height, length, width, *args):
    box_size = height * length * width
    cubes_left = 0
    for arg in args:
        if arg == 'Finish':
            break
        if box_size >= int(arg):
            box_size -= int(arg)
        else:
            arg -= box_size
            cubes_left += arg
            box_size = 0
    if box_size:
        return f'There is free space in the box. You could put {box_size} more cubes.'
    else:
        return f'No more free space! You have {cubes_left} more cubes'


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))



﻿#There is a robotics factory. The current project is assembly-line robots.
# Each robot has a processing time – it is the time in seconds the robot needs to process a product. When a robot is free,
# it should take a product for processing and log its name, product, and processing start time.
# Each robot processes a product coming from the assembly line. A product is coming from the line each second (so the first
# product should appear at [start time + 1 second]). If a product passes the line and there is not a free robot to take it,
# it should be queued at the end of the line again.
# The robots are standing in the line in the order of their appearance.
# Input
# · On the first line, you will receive the robots' names and their processing times in the format "robotName-processTime;robotName-processTime;robotName-processTime..."
# · On the second line, you will get the starting time in the format "hh:mm:ss"
# · Next, until the "End" command, you will get a product on each line.
# Output
# · Every time a robot takes a product, you should print: "{robotName} - {product} [hh:mm:ss]"

from collections import deque


def read_robots():
    result = {}
    robots_input = input().split(';')
    for robot_input in robots_input:
        robot_details = robot_input.split('-')
        name = robot_details[0]
        processing_time = int(robot_details[1])
        result[name] = processing_time
    return result


def to_seconds(hours, minutes, seconds):
    return hours * 60 * 60 + minutes * 60 + seconds


def read_products():
    result = deque()
    while True:
        line = input()
        if line == 'End':
            break
        result.append(line)
    return result


def to_str_time(time_in_seconds):
    hours = time_in_seconds // 3600
    minutes = (time_in_seconds % 3600) // 60
    seconds = (time_in_seconds % 3600) % 60
    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'


robots = read_robots()
available_robots = [k for k in robots.keys()]
processing_robots = {}

starting_time_parts = [int(x) for x in input().split(':')]
time_in_seconds = to_seconds(starting_time_parts[0], starting_time_parts[1], starting_time_parts[2])

products = read_products()

while products:
    time_in_seconds = (time_in_seconds + 1) % (24 * 60 * 60)
    
    for robot_name in [k for k in processing_robots.keys()]:
        processing_robots[robot_name] -= 1
        if processing_robots[robot_name] == 0:
            processing_robots.pop(robot_name)

    current_product = products.popleft()
    for robot_name in available_robots:
        if robot_name not in processing_robots:
            print(f'{robot_name} - {current_product} [{to_str_time(time_in_seconds)}]')
            processing_robots[robot_name] = robots[robot_name]
            break
    else:
        products.append(current_product)



def students_credits(*args):
    total_credits = 0
    credits_info = dict()
    result_strings = []

    for arg in args:
        course_name, course_credits, max_points, student_points = arg.split('-')
        current_percentage = int(student_points) / int(max_points)
        student_current_credits = current_percentage * int(course_credits)
        total_credits += student_current_credits
        credits_info[course_name] = student_current_credits

    if total_credits >= 240:
        result_strings.append(f'The student gets a diploma with {total_credits:.1f} credits')
    else:
        result_strings.append(f'Student needs {240 - total_credits:.1f} credits more for a diploma.')
    sorted_points_info = sorted(credits_info.items(), key=lambda x: -x[1])

    for course, points in sorted_points_info:
        result_strings.append(f'{course} - {float(points):.1f}')

    return '\n'.join(result_strings)

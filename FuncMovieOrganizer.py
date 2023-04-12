def movie_organizer(*args):
    movies_dict = {}
    for arg in args:
        movie = arg[0]
        genre = arg[1]
        if genre not in movies_dict.keys():
            movies_dict[genre] = [movie]
        else:
            movies_dict[genre].append(movie)

    sorted_result = {key: value for key, value in sorted(movies_dict.items(), key=lambda x: (-len(x[1]), x[0]))}
    sorted_values = {x: sorted(sorted_result[x]) for x in sorted_result.keys()}
    result = ''
    for key, value in sorted_values.items():
        result += f'{key} - {len(sorted_values[key])}\n'

        for movie in value:
            result += f'* {movie}\n'
    return result


print(movie_organizer(
    ("The Matrix", "Sci-fi")))



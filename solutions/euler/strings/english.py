LITERAL = ['first', 'second', 'third', 'fourth', 'fifth']


def convert_to_english(number):
    string_number = str(number)

    if 10 < number < 20:
        return string_number + 'th'

    return string_number + {
        '1': 'st',
        '2': 'nd',
        '3': 'rd',
    }.get(string_number[-1], 'th')

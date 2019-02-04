big_numbers = [(12, 'billion(s)'),
               (9, 'milliard(s)'),
               (6, 'million(s)'),
               (3, 'thousand(s)')]


def format_big_number(number):
    try:
        number = int(number)
    except ValueError:
        return number
    for i, name in big_numbers:
        if number >= 10**i:
            number = number // 10**i
            number = str(number) + ' ' + name
            break
    return number


def format_big_numbers(planets):
    for planet in planets:
        planet['population'] = format_big_number(planet.get('population'))

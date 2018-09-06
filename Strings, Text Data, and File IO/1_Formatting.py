def convert(degrees_celcius):
    degrees_fahrenheit = degrees_celcius * 1.8 + 32
    return degrees_fahrenheit


def table():
    print('{:>3} {:} {:>3}'.format('F', '   ',  'C'))
    for i in range(-30, 40, 10):
        print('{:>5}  {:>5}'.format(convert(i), i))


table()

def get_number_from_string(string: str):
    return int(string[:6])


with open('kaartnummers.txt', 'r') as file:
    i = 0
    line_with_highest_number = ''
    for line in file:
        i += 1
        number = get_number_from_string(line)

        highest_line = get_number_from_string(line_with_highest_number)
        if number > highest_line:
            line_with_highest_number = line
    file_length = i
    print(line_with_highest_number)
    print('Dit bestand heeft ' + str(file_length) + ' regels.')


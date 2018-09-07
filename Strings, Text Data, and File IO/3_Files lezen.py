with open('kaartnummers.txt', 'r') as file:
    i = highest_line = highest_number = 0

    for line_number, line in enumerate(file):
        i += 1

        if int(line[:6]) > highest_number:
            highest_number = int(line[:6])
            highest_line = line_number
    file.close()

print('Dit bestand heeft ' + str(i) + ' regels')
print('Het grootste kaartnummer is: ' + str(highest_number) + ' en dat staat op regel ' + str(highest_line))

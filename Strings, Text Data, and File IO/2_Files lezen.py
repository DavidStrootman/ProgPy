with open('kaartnummers.txt', 'r') as file:
    for line in file:
        number = line[:5]
        name = line[7:-1]
        print(name + ' heeft kaarnummer: ' + number)

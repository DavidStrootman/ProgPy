number = 1
list = []
while not(0 == number):
    number = int(input('Voer een nummer in'))
    list.append(number)
print('Er zijn ' + str(len(list) - 1) + ' getallen ingevoerd, de som is: ' + str(sum(list)) + '.')

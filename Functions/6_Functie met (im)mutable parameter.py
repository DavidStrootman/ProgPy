lijst = ['a', 'b', 'c']


def wijzig(letterlijst):
    letterlijst.clear()
    letterlijst += ['d', 'e', 'f']


print(lijst)
wijzig(lijst)
print(lijst)

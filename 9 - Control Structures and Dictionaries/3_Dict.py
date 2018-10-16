cijfers = {
    'Jan': 2,
    'Stephen': 8,
    'Lee': 4,
    'Leon': 10,
    'Reed': 7,
    'Dirk': 9,
    'Martha': 7,
    'Kathleen': 2
}

for name, grade in cijfers.items():
    if grade > 9:
        print(str(name) + ': ' + str(grade))

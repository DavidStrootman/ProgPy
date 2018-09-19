def namen() -> print:
    names = {}
    name = 0

    while name != '':
        name = input('Voer een naam in: ')
        if 1 < len(name):
            if name not in names:
                names[name] = 1
            else:
                names[name] += 1
    for name, count in names.items():
        print(
            "Er {} {} student{} met de naam "
            .format('zijn' if 1 < count else 'is', count, 'en' if 1 < count else '')
            + name
        )
    if 1 > len(names):
        print('Er zijn geen namen opgegeven')


namen()

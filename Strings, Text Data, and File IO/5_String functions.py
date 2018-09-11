random_input = input('Voer een willekeurige zin in:')


def gemiddelde():
    length = len(random_input.replace(' ', ''))
    words = len(random_input.split())
    print(length / words)


gemiddelde()

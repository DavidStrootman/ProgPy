getallen = [4, 5, 3, -81]


def kwadraten_som(grondgetallen):
    squares_sum = 0

    for getal in grondgetallen:
        if 0 < getal:
            squares_sum += getal * getal

    return squares_sum


print(kwadraten_som(getallen))

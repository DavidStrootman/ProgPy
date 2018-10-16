def som(getallen_lijst):
    combined_number = 0

    for number in getallen_lijst:
        combined_number += number

    return combined_number


print(som([20, 30, 2]))

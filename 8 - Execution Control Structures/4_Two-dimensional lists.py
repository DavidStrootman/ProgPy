studentencijfers = [[95, 92, 86], [66, 75, 54], [89, 72, 100], [34, 0, 0]]


def gemiddelde_per_student(cijfers: list):
    gemiddelden = []

    for studenten in cijfers:
        gemiddelden.append(sum(studenten) / len(studenten))
    return gemiddelden


def gemiddelde_van_alle_studenten(cijfers: list):
    gemiddelden = gemiddelde_per_student(cijfers)

    return sum(gemiddelden) / len(gemiddelden)


print(str(gemiddelde_per_student(studentencijfers)))
print(str(gemiddelde_van_alle_studenten(studentencijfers)))

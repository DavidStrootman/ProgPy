def standaardprijs(afstandKM: float):
    if 0 >= afstandKM:
        return 0
    if 50 < afstandKM:
        return 15 + 0.60 * afstandKM
    return afstandKM * 0.80


def ritprijs(leeftijd: int, weekendrit: bool, afstandKM: float):
    prijs = standaardprijs(afstandKM)
    discount = 0

    if 65 <= leeftijd or 12 > leeftijd:
        if weekendrit:
            discount = 0.35
        else:
            discount = 0.3
    elif weekendrit:
        discount = 0.4
    return round(prijs * (1 - discount), 2)


print(ritprijs(20, True, 50.1))

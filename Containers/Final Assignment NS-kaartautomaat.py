def inlezen_beginstation(stations):
    while True:
        station = input("Beginstation: ")

        if station in stations:
            return station
        else:
            print("Dit station bestaat niet!")

def inlezen_eindstation(stations, beginstation):
    while True:
        station = input("Eindstation: ")

        if station in stations:
            if stations.index(beginstation) > stations.index(station):
                print("Dit eindstation is voor het begin station")
            else:
                return station
        else:
            print("Dit station bestaat niet!")

def omroepen_reis(stations, beginstation, eindstation):
    begin_idx = stations.index(beginstation)
    eind_idx = stations.index(eindstation)

    print("Het beginstation {} is het {}e station in het traject.".format(beginstation, begin_idx + 1))
    print("Het eindstation {} is het {}e station in het traject.".format(eindstation, eind_idx + 1))

    afstand = eind_idx - begin_idx
    print("De afstand bedraagt {} station(s).".format(afstand))

    prijs = afstand * 5
    print("De prijs van het kaartje is {} euro.".format(prijs))

    print("Jij stapt in de trein in: {}".format(beginstation))

    for i in range(begin_idx + 1, eind_idx):
        print(" - {}".format(stations[i]))

    print("Jij stapt uit in: {}".format(eindstation))

stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', '’s-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']

beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)

def inlezen_beginstation(stations):
    beginstation = input('Vul een beginstation in: ')

    while beginstation not in stations:
        print('Beginstation komt niet voor in de lijst van stations.')
        beginstation = input('Vul een beginstation in: ')
    return beginstation


def inlezen_eindstation(stations, beginstation):
    eindstation = input('Vul een eindstation in: ')

    if eindstation in stations:
        while stations.index(beginstation) > stations.index(eindstation):
            print('Eindstation komt voor het beginstation.')
            # de var eindstation shadowt de var hogerop, maar dit helpt de while compact te houden.
            eindstation = input('Vul een eindstation in: ')

    return eindstation


def omroepen_reis(stations, beginstation, eindstation):
    begin_id = stations.index(beginstation)
    eind_id = stations.index(eindstation)
    afstand = eind_id - begin_id

    print('Het beginstation', beginstation, 'is het', begin_id, 'station in het traject.')
    print('Het Eindstation', eindstation, 'is het', eind_id, 'station in het traject.')
    print('De afstand bedraagt', afstand, 'station(s)')
    print('De prijs van het kaartje is', afstand * 5, 'euro\n')

    print('Jij stapt in de trein in:', beginstation)
    for i in range(begin_id + 1, eind_id):
        print('-', stations[i])
    print('Jij stapt uit in: ', eindstation)

stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', '’s-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)

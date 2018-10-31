import xmltodict

with open("stations.xml", "r") as f:
    xmldict = xmltodict.parse(f.read())

    print("Dit zijn de codes en types van de 4 stations:")

    for station in xmldict["Stations"]["Station"]:
        print("{:<4} - {}".format(station["Code"], station["Type"]))

    print("\nDit zijn alle stations met één of meer synoniemen:")

    for station in xmldict["Stations"]["Station"]:
        if station["Synoniemen"] is not None:
            print("{:<4} - ".format(station["Code"]), end="")
            print(*station["Synoniemen"]["Synoniem"], sep=", ")  # Note the star

    print("\nDit is de lange naam van elk station:")

    for station in xmldict["Stations"]["Station"]:
        print("{:<4} - {}".format(station["Code"], station["Namen"]["Lang"]))

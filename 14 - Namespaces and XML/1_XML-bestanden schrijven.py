# De opdracht heet XML-bestanden schrijven maar inhoudelijk moet je alleen het bestand lezen en printen

import xmltodict

with open("artikelen.xml", "r") as f:
    xmldict = xmltodict.parse(f.read())

    for artikel in xmldict["artikelen"]["artikel"]:
        print(artikel["naam"])

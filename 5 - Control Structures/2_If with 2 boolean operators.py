def get_bool(prompt):
    while True:
        try:
            return {"ja": True, "nee": False}[input(prompt).lower()]
        except ValueError:
            print("Voer aub ja of nee in!")


def get_age():
    while True:
        try:
            return int(input('Geef je leeftijd op: '))
        except ValueError:
            print('Geen correcte leeftijd opgegeven')


age = get_age()

dutchPassport = get_bool('Heb je een Nederlands paspoort? [ja/nee] ')

if 18 <= age and dutchPassport:
    print('Gefeliciteerd, je mag stemmen!')
else:
    print('Je mag helaas niet stemmen.')

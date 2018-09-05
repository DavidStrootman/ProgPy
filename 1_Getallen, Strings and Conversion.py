cijferICOR = 7
cijferPROG = '8,5'
cijferCSN = 7
cijfers = [cijferICOR, cijferPROG, cijferCSN]

for key, value in enumerate(cijfers):
    if isinstance(value, str):
        cijfers[key] = float(value.replace(',', '.'))

gemiddelde = sum(cijfers) / len(cijfers)
beloning = sum(cijfers) * 30
overzicht = 'Mijn gemiddelde van ' + str(gemiddelde) + ' geeft mij een ondersteuning van €' + str(beloning) + '.'

print(overzicht)

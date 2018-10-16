invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
sorted_invoer = sorted(list(map(int, invoer.split('-'))))

print(sorted_invoer)
print('Grootste getal: ' + str(max(sorted_invoer)) + ' en kleinste getal: ' + str(min(sorted_invoer)))
print('Aantal getallen: ' + str(len(sorted_invoer)) + ' en som van getallen: ' + str(sum(sorted_invoer)))
print('Gemiddelde: ' + str(sum(sorted_invoer) / len(sorted_invoer)))

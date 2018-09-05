tupleShadow = ['A', 'C', 'B', 'B', 'C', 'A', 'C', 'C', 'B', 'D']
sortedList = sorted([[x, tupleShadow.count(x)] for x in set(tupleShadow)])
sortedValues = []

[sortedValues.append(value) for key, value in sortedList]

print()

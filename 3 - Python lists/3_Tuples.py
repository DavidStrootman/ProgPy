from collections import Counter

tuple_shadow = ('A', 'C', 'B', 'B', 'C', 'A', 'C', 'C', 'B', 'D')
sorted_list = list(Counter(sorted(tuple_shadow)).values())

print(sorted_list)

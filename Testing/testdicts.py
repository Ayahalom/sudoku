d = dict({1: {8, 9, 4}, 2: {9, 4}, 3: {9, 4}, 4: {5, 7}})
d2 = {i: set() for i in range(1, 10)}

for key, values in d.items():
    for value in values:
        d2[value].add(key)
print(d2)

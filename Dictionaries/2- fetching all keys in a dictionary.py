dict1 = {'x': 10, 'y': 8}

print(dict1.keys())
dict_keys = [x[0] for x in dict1.items()]
print(dict_keys)
print(dict1.items())

dict_keys2 = [x for x in dict1]
print(dict_keys2)

print([dict1])

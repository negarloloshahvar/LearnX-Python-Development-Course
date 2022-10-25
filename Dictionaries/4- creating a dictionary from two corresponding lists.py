keys = ['name', 'age', 'location']
values = ['Negar', 26, 'london']

# my_dict = {keys[x]: values[x] for x in range(len(keys))}
my_dict = {}
# for x in range(len(keys)):
#     my_dict[keys[x]] = values[x]
my_dict = dict(zip(keys, values))
print(my_dict)
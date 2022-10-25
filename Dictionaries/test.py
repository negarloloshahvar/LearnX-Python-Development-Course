my_dict = {'name': 'Negar', 'age': 26, 'location': 'london'}

# dict_values = my_dict.values()

# dict_values = []
# for key, value in my_dict.items():
#     dict_values.append(value)

dict_values = []
for key in my_dict.keys():
    dict_values.append(my_dict[key])

print(dict_values)



# for key, value in my_dict.items():
#     print(key)

dict_keys = []
# for keys, value in my_dict.items():
#     dict_keys.append(keys)

# for item in my_dict:
#     print(item)

# print(dict_keys)

name = my_dict.get('major', 'Industrial Engineer')
print(name)

print(my_dict)

hobby = my_dict.get('hobby')
# my_dict['name'] = 'Abtin' if 'name' not in my_dict else None
# my_dict.set('name', 'Abtin', update= False)
# my_dict['name'] = 'Abtin'
my_dict.setdefault('husband', 'Abtin')
print(my_dict)

my_list = [123, 'neg', 89.5]
my_list.pop()
print(my_list)
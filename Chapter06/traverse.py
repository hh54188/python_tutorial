person = {
    "name": "liguangyi",
    "age": 27,
    "city": "beijing"
}

print('---------- items() ----------')
for key, value in person.items():
    print(key + ", " + str(value))

print('---------- keys() ----------')
for key in person.keys():
    print(key)

print('---------- values() ----------')
for value in person.values():
    print(value)

print(person.keys())  # dict_keys(['name', 'age', 'city'])
print(list(person.keys()))  # ['name', 'age', 'city']

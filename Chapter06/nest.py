liguangyi = {
    "name": "liguangyi",
    "age": "27",
    "city": "beijing"
}

mengxiao = {
    "name": "mengxiao",
    "age": "28",
    "city": "dongbei"
}

guomiao = {
    "name": "guomiao",
    "age": "29",
    "city": "anhui"
}

persons = [liguangyi, mengxiao, guomiao]

for person in persons:
    print(person["name"] + '----------')
    for key, value in person.items():
        print(key + ": " + value)

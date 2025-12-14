# dictionary={
#     "key1" : "value1"
#     "key2" : "value2"

# }

person={
    "name":"Zahra",
    "age":20,
    "city": "kabul"
}
print(person)
print(person["name"])
print(person["age"])

for key in person.keys():
    print(key)

for value in person.values():
    print(value)


for key,value in person.items():
    print(f"{key} ...... {value}")



students={
    "student1": {"Name": "Hassina", "age":18},
    "student2": {"Name": "fatima", "age":18},
    "student3": {"Name": "zahra", "age":18},
    "student4": {"Name": "fatima", "age":18},
    "student5": {"Name": "fatima", "age":18}
}

print(students)
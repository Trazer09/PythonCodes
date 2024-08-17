person1 = {
"first-name" : "Sam",
"last-name"  : "Altman",
"age": 28,
"city": "New York"
}

person2 = {
"first-name" : "Tim",
"last-name"  : "Cook",
"age": 34,
"city": "Melbourne"
}

person3 = {
"first-name" : "Steve",
"last-name"  : "Smith",
"age": 32,
"city": "Los Angeles"
}

people = [person1, person2, person3]

for person in people:
    full_name = f"{person['first-name']} {person['last-name']}"
    print(f"Name: {full_name}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")
    print()

people = [
     {"name":"Harry", "house":"Gryffindor"},
     {"name":"Hermoine", "house":"Slytherin"},
     {"name":"Draco", "house":"Ravenclaw"}
]

people.sort(key = lambda person: person["house"])
print(people)
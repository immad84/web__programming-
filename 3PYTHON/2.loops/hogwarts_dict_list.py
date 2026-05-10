students = [
    {'name': 'Harry', 'house': 'Gryffindor', 'patronus': 'Otter'},
    {'name': 'Hermione', 'house': 'Gryffindor', 'patronus': 'Stag'},
    {'name': 'Ron', 'house': 'Gryffindor', 'patronus': 'Jack Russel Terier'},
    {'name': 'Draco', 'house': 'Slytherin', 'patronus': None}
]

for student in students:
    print(f'{student['name']:<15}', f'{student['house']:<15}', student['patronus'])
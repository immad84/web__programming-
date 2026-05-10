students = []
with open('students.csv') as file:
    for row in file:
        name, house = row.rstrip().split(',')
        students.append({'name': name, 'house': house})

# for line in sorted(lines):
#     name, house = line.rstrip().split(',')
#     print(f'{name} is in {house}')

for student in sorted(students, key=lambda student: student['name']):
    print(f'{student["name"]} is in {student["house"]}')

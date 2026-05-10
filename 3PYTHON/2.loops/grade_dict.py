grades = {
    'math': 89,
    'cs': 95, 
    'statistics': 87
    }

for subject, grade in grades.items():
    print(f'{subject} : {grade}')

for grade in range(len(grades)):
    print(grade)
import csv

# with open('students_v2.csv') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(f'{row[0]} from {row[2]}')

students = []
with open('students_v2.csv') as file:
    dictReader = csv.DictReader(file)
    for row in dictReader:
        # print(f'{row["Name"]} from {row["Residence"]} is in {row["House"]}')
        students.append(row)

for student in sorted(students, key = lambda student: student["Name"]):
    print(f'{student["Name"]} from {student["Residence"]} is in {student["House"]}')

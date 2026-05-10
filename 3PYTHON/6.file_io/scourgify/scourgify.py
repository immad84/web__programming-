import csv
import sys
from tabulate import tabulate


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    students = []
    sorted_students = []

    try:
        firstArg, secondArg, thirdArg = sys.argv
        with open(secondArg) as file, open(thirdArg, "w") as after:
            reader = csv.DictReader(file)
            writer = csv.DictWriter(after, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for row in reader:
                last, first = row["name"].split(",")
                student = {
                    "first": first.strip(),
                    "last": last.strip(),
                    "house": row["house"],
                }
                students.append(student)
                writer.writerow(student)
    except FileNotFoundError as e:
        sys.exit(f"Could not read {e.filename}")

    # for student in sorted(students, key=lambda student: student['first']):
    #     print(f'{student['first']:<15}{student['last']:<15}{student['house']:>15}')

    for student in sorted(students, key=lambda student: student["first"]):
        sorted_students.append(student)

    print(tabulate(sorted_students, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    main()

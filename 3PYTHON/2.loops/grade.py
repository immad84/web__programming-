def main():
    grades = []
    while True:
        grade = int(input('Enter grade '))
        if grade < 0:
            break
        print(get_grades(grade))
        grades.append(grade)
    print('Avg Grade:', get_grades_total(grades))

def get_grades_total(grade_list):
    total = 0
    count = 0
    for i in grade_list:
        total += i
        count += 1
    return (total / count)

def get_grades(g):
    if 90 <= g <= 100:
        return 'Grade: A'
    elif 80 <= g < 90:
        return 'Grade: B'
    elif 70 <= g < 80:
        return 'Grade: C'
    elif 60 <= g < 70:
        return 'Grade: D'
    else:
        return 'Grade: F'

if __name__ == '__main__':
    main()
def main():
    students = ['Harry', 'Hermione', 'Ron']
    print_students(students)

def print_students(s):
    for i in range(len(s)):
        print(f'{i + 1:<10}', s[i])

if __name__ == '__main__':
    main()

def main():
    print_row()
    print_brick()

def print_brick():
    for _ in range(3):
        for j in range(3):
            print(f'# ', end=' ')
        print()

def print_question_brick():
    for i in range(1, 4):
        for j in range(1, 10):
            if i % 2 == 0 and j % 2 == 0:
                print('? ', end= ' ')
            else:
                print('# ', end= ' ')
        print()

def print_row():
    print_question_brick()
        

if __name__ == '__main__':
    main()

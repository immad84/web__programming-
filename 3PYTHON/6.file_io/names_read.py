import sys

def main():
    names = []
    if len(sys.argv) > 1:
        if sys.argv[1] != '--s' and sys.argv[1] != '--sort':
            sys.exit('Invalid Usage')
        if sys.argv[2] != 'asc' and sys.argv[2] != 'des':
            sys.exit('Invalid Usage')

        with open('names.txt', 'r') as file:
            for line in file:
                names.append(line.rstrip())

        if sys.argv[2] == 'asc':
            for name in sorted(names):
                bar = '*' * names.index(name) if names.index(name) != 0 else '@'
                print(f'{names.index(name):<5}{name:<15}{bar}')
        else:
            for name in sorted(names, reverse=True):
                bar = '*' * names.index(name) if names.index(name) != 0 else '@'
                print(f'{names.index(name):<5}{name:<15}{bar}')
    else:
        with open('names.txt', 'r') as file:
            for line in file:
                names.append(line.rstrip())

        for name in names:
            print(f'{names.index(name):<5}{name:<15}{'*' * names.index(name)}')

if __name__ == '__main__':
    main()

import sys

def main():
    if len(sys.argv) == 2:
        hello(sys.argv[1])
        print()
        goodby(sys.argv[1])

def hello(name):
    print(f'Hello, {name}')

def goodby(name):
    print(f'Goodby, {name}')

if __name__ == '__main__':
    main()
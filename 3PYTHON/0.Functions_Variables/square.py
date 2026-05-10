def main():
    # get a numner from user
    x = int(input('What\'s x ? '))
    # print the return value of square function
    print('x squared is ', square(x))

def square(n):
    return n ** 2  # n * n or pow(n, 2) do the same thing

main()
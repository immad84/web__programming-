# """This is a Multi-Line Comment. Comments serve as pseudocode"""
# # Get the user name.
# name = input('What\'s your name ? ').strip().title()
# # store welcome string inside string variable.
# string = f'Hello, \'My Friend\' {name}. What\'s Up\
# .\tHow can I help ? '
# # print the welcome message.
# print(string, end='\n')

def main():
    name = input('What\'s your name ? ')
    print(greet_user(name))

def greet_user(n):
    string = f'hello, \'my friend\' {n}. what\'s up.\
how can i help ? '
    string = string.title()
    return string

main()

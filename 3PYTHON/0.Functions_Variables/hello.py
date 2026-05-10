# define a main function
def main():
    # get user name
    name = input('What\'s your name ? ')
    # call the greet function to greet the user.
    greet(name)
    

# define the greet function
def greet(to = 'World'):
    # print the greeting message.
    print('Hello,', to)

main()
# get the user name
name = input('What\'s your name ? ')
name = name.strip().title()

first, last = name.split(' ')

# say hello to the user
print('Hello, ', end='')
print(last)

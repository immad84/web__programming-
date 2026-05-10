url = input('URL: ')
# username = url.replace('https://twitter.com', '')
username = url.removeprefix('https://twitter.com/')
print(f'User Name: {username}')
import re

name = input('What\'s your name ? ')
if matches := re.search(r'^(.+)[, ](.+)$', name, flags=re.IGNORECASE):
    last, first = matches.groups()
    name = f"{first} {last}"

print(f'Hello, {name}')


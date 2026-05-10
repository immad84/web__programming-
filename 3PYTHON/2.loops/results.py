results = ['mario', 'luigi']

results.append('princess')
results.append('yoshi')
results.remove('yoshi')
results.append('koopa troopa')
results.append('yoshi')
results.append(['toad', 'bowser', 'donkey kong jr'])
results.remove(['toad', 'bowser', 'donkey kong jr'])
results.extend(['toad', 'bowser', 'donkey kong jr'])
results.reverse()
results.remove('mario')
results.insert(0, 'mario')

print(results)
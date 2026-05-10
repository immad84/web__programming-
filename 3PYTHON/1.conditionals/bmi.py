weight = float(input('What\'s your weight ? '))
height = float(input('What\'s your height ? '))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print('Underweight')
elif bmi < 24.9:
    print('Normalweight')
elif bmi < 29.9:
    print('Overweight')
else:
    print('Obisity')
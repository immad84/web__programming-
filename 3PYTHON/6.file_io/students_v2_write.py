import csv 

# Luna,Lovegood House,Ravenclaw
# Cedric,Diggory House,Hufflepuff
# Pansy,Parkinson Manor,Slytherin

name = input('What\'s student Name ? ')
residence = input('What\'s student Residence ? ')
house = input('What\'s student house ? ')

with open('students_v2.csv', 'a') as file:
    dictWriter = csv.DictWriter(file, fieldnames=['Name', 'Residence', 'House'])
    dictWriter.writerow({'Residence': residence, 'Name': name, 'House': house})

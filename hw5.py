import random as rd
import csv
import time

colors = {1: 'blue', 2: 'red', 3: 'cyan', 4: 'orange', 5: 'violet',
          6: 'green', 7: 'purple', 8: 'yellow', 9: 'indigo', 10: 'teal'}

animals = {1: 'monkey', 2: 'whale', 3: 'shark', 4: 'elephant',
           5: 'lion', 6: 'parrot', 7: 'ant', 8: 'horse', 9: 'dog', 10: 'snake'}

# reading all previous secret names or creating file if doesn't exist
contents = []
previousCodes = {}
try:
    with open('codenames.csv', 'r') as f:
        csvReader = csv.reader(f)
        for row in csvReader:
            contents.append(row)
            previousCodes[row[1]] = 1
        f.close()
except:
    with open('codenames.csv', 'x') as f:
        csvWriter = csv.writer(f)
        contents.append(['Name', 'Secret Code Name'])
        f.close()


print('Please enter your name:')
name = input()
time.sleep(.5)
print('Thank you...')

# get secret name and verify it doesn't exist
switch = 0
while switch == 0:
    color = colors[rd.randint(1, 10)]
    animal = animals[rd.randint(1, 10)]
    if previousCodes.get(f'{color} {animal}'):
        switch = 0
    else:
        switch = 1
        contents.append([name, f'{color} {animal}'])

time.sleep(1)
print(f'Your secret code name is {color} {animal}')

# write all names back to file
with open('codenames.csv', 'w') as f:
    csvWriter = csv.writer(f)
    csvWriter.writerows(contents)
f.close()

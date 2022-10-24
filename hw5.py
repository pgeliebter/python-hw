# The SSHPP (Secret Society of Honors Python Programmers) wants to give students a silly code name when they join the club.  The club wants to assign to each person a color and an animal. For example a member's name could be "orange seal" or "gray parrot".

# Create a dictionary of colors. each one has a numeric key and a color. For example they may have a key of 1 with a value of blue, a key of 2 with a value of red, etc..  Create a dictionary of animals, using the same idea. A sequential key number followed by an animal. For the purpose of testing, create 10 animals and 10 colors.

# Accept the user input of the member's name.  Then using a random number for each dictionary, generate a name.

# The member name, the color and the animal should be saved to a CSV file. A message should also sent to the user telling them what their code is.

# For this exercise, you will not need code to check if the combination already exists in the file. You can earn 5 extra credit points if you enhance the above to check if the combination already exists and have the code automatically try again until it finds a unique code.  The code should do this without prompting the user again

import random as rd
import csv
import time

colors = {1: 'blue', 2: 'red', 3: 'cyan', 4: 'orange', 5: 'violet',
          6: 'green', 7: 'purple', 8: 'yellow', 9: 'indigo', 10: 'teal'}

animals = {1: 'monkey', 2: 'whale', 3: 'shark', 4: 'elephant',
           5: 'lion', 6: 'parrot', 7: 'ant', 8: 'horse', 9: 'dog', 10: 'snake'}

# reading all previous secret names
contents = []
previousCodes = {}
with open('codenames.csv', 'r') as f:
    csvReader = csv.reader(f)
    for row in csvReader:
        contents.append(row)
        previousCodes[row[1]] = 1
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

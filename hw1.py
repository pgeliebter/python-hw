import random as rd

# problem 1
print("Problem 1: ")
for i in range(1, 10, 2):
    print(i)

# problem 2
print("\nProblem 2: ")
for i in range(10, 0, -1):
    print(i)

# problem 3
print("\nProblem 3: ")
i = 10
while (i > 0):
    print(i)
    i -= 1

# problem 4
print("\nProblem 4: ")
for i in range(0, 10):
    print(rd.randint(1, 100))

# extra credit
print("\nExtra Credit:")
barcode = 98201
output = ''
for i in range(len(str(barcode))):
    output += '|' * int(str(barcode)[i])
    output += ' '
print(output)

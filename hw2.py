
import csv
print("Problem 1: ")
part1File = open('hw2testfile.csv', 'r')
lines = part1File.readlines()
total = 0
for line in lines:
    try:
        int(line)
        total += int(line)
    except:
        print("A non number cell has been skipped")
        continue
print(total)
part1File.close()


print("\nProblem 2: ")
file = open('birthwt.csv', 'r')
csvReader = csv.reader(file, delimiter=',')
smokeIndex = 0
for i, key in enumerate(csvReader.__next__()):
    if key == "smoke":
        smokeIndex = i
smokerTotal = 0
for row in csvReader:
    if int(row[smokeIndex]) == 1:
        smokerTotal += 1
print(smokerTotal)

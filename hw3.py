import csv

print("Problem 1: ")


def meanCalc(file):
    openedFile = open(file, 'r')
    csvReader = csv.reader(openedFile, delimiter=',')
    ageIndex = 2
    csvReader.__next__()
    mean = [0, 0]
    for row in csvReader:
        mean[0] += int(row[ageIndex])
        mean[1] += 1
    return (mean[0]/mean[1])


# calling and printing the output of function
print(meanCalc('birthwt.csv'))

print("\nProblem 2: ")


def meanCalc(file, colIndex):
    openedFile = open(file, 'r')
    csvReader = csv.reader(openedFile, delimiter=',')
    csvReader.__next__()

    mean = [0, 0]
    for row in csvReader:
        mean[0] += int(row[colIndex])
        mean[1] += 1
    return (mean[0]/mean[1])


# calling and printing the output of function
print(meanCalc('birthwt.csv', 3))


# 3-  Create a function to read in the rainfall csv. Read each row and convert the average rainful to inches.  Write the city, the rain (in cm) and inches to a new file. (include column headings)

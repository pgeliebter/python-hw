import csv

print("Problem 1: ")


def meanCalc(file):
    openedFile = open(file, 'r')
    csvReader = csv.reader(openedFile, delimiter=',')
    ageIndex = 2
    # call next row to skip header
    csvReader.__next__()
    mean = [0, 0]
    for row in csvReader:
        mean[0] += int(row[ageIndex])
        mean[1] += 1
    openedFile.close()
    return (mean[0]/mean[1])


# calling and printing the output of function
print(meanCalc('birthwt.csv'))

print("\nProblem 2: ")


def meanCalc(file, colIndex):
    openedFile = open(file, 'r')
    csvReader = csv.reader(openedFile, delimiter=',')
    # call next row to skip header
    csvReader.__next__()
    mean = [0, 0]
    for row in csvReader:
        mean[0] += int(row[colIndex])
        mean[1] += 1
    openedFile.close()
    return (mean[0]/mean[1])


# calling and printing the output of function
print(meanCalc('birthwt.csv', 3))


def createRainfallInIN(file):
    openedFile = open(file, 'r')
    csvReader = csv.reader(openedFile, delimiter=',')
    try:
        newFile = open('newRainfall.csv', 'w')
    except:
        newFile = open('newRainfall.csv', 'x')
    csvWriter = csv.writer(newFile)
    # call next row to skip header
    csvReader.__next__()
    newHeader = ['city', 'rainfall in CM', 'rainfall in IN']
    csvWriter.writerow(newHeader)
    for row in csvReader:
        city = row[0]
        rainfallInCM = float(row[1])
        rainfallInIN = float(row[1])/2.54
        newRow = [city, rainfallInCM, rainfallInIN]
        csvWriter.writerow(newRow)
    openedFile.close()
    newFile.close()


createRainfallInIN('rainfallInCM.csv')
print("\nProblem 3: new file created")

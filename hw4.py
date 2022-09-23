
# 3- Write a function that will check if all items in a list are numeric. Hint: think about exception handlers. test with a list that has all numerics and a list that does not have all numerics.


import csv


def checkIfPrime(num):
    isPrime = True
    if num == 1:
        return False
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                isPrime = False
                break
    return isPrime


def writeToFile(enumData, filename):
    try:
        newFile = open(filename, 'w')
    except:
        newFile = open(filename, 'x')
    csvWriter = csv.writer(newFile)
    for item in enumData:
        csvWriter.writerow([item])


def primeNumbers(numOfPrimes):
    primes = []
    startNum = 2
    while len(primes) < numOfPrimes:
        if checkIfPrime(startNum):
            primes.append(startNum)
        startNum += 1
    writeToFile(primes, 'list_of_primes.csv')
    return primes


print("Problem 1: new file created and here is list:")
print(primeNumbers(20))

print("\nProblem 2: ")


def reverseList(list):
    newList = []
    index = len(list) - 1
    while index >= 0:
        newList.append(list[index])
        index -= 1
    return newList


listToReverse = [10, 12, "hello",
                 "this should now be in beginning"]
print(reverseList(listToReverse))

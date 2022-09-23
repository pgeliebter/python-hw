# 1- Create a function that will return a list of n prime numbers (where n is the number of primes to calculate).  Add a function to write the list out to a file  You can use some of the earlier code used this semester as a starting point. For example, if we pass the function a parmeter of 5, it will return the first 5 prime numbers. Print out the list at the end.
# 2- Create a function that receives a list of values and reverses the order of the list into a new list and returns the new list. Use loops to accomplish this and not built-in functions. for exampe,
# 3- Write a function that will check if all items in a list are numeric. Hint: think about exception handlers. test with a list that has all numerics and a list that does not have all numerics.


# def primeNumbers(numOfPrimes):
# primes = []
#  while len(primes) < numOfPrimes:
#       # print(primes, numOfPrimes)
#       startNum = 4
#       for divisor in range(2, startNum):
#           print(divisor)
#           if (startNum % divisor) == 0:
#               flag = True
#       if flag != True:
#           primes.append(startNum)
#       startNum += 1
#   return (primes)

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


print(primeNumbers(20))

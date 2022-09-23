# Using the code from this weeks lecture as a guide, write code for the following questons:

# 1- Download the attached file (hw2testfile.csv) into your python home directory. Look through the file (notice how one row of data contains non-numeric data) . Write code to total up the values of the file and print that final value. You will need to add an exception handler to handle the non-numeric data.   Keep the exception handler simple.  You can just print a line saying "A non numeric value has been ignored"

# 2- Download the attached birthwt.csv file.  Determine how many smokers there are in the file.  This is all rows where smoke = 1.  Hints:  An if statement is needed in the loop. remember to convert the column to an integer before testing equivalence

# NOTE: Please do not change the names of the input files. Also, please place your input files in your Python directory.  The path on your computer will not match mine.  Adhering to these will help speed up the grading process.

print("Problem 1: ")
part1File = open('hw2testfile.csv', 'r')
lines = part1File.readlines()
total = 0
for line in lines:
    try:
        int(line)
        total += int(line)
    except:
        print("A non number has been skipped")
        continue
print(total)

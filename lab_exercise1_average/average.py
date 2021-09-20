# Travis McDaniel
# 12/10/2020
# This program uses a file containing integers, reads and calculates the average of integers

# Using the File concepts discussed in class:
# Create a text file named numbers.txt containing a series of integers.
# The text file must be saved in this assignment's Python folder and submitted with the python program (.py) file.
# Write a program that reads and calculates/print the average of all the integer
# numbers stored in the file (Hint: use a for loop to read the values)

# WARNING---- make sure file does not have blank spaces or you will get
# Traceback (most recent call last):
#   File "C:\Users\mcdt7\PycharmProjects\lab_exercise1_average\average.py", line 18, in <module>
#     amount = float(line.rstrip('\n'))               # stores and makes value a float
# ValueError: could not convert string to float: ''


total = 0
numbers = 0

infile = open('numbers.txt', 'r')                   # open the numbers file for reading

for line in infile:                                 # for loop and gets numbers in file
    print(line.rstrip('\n'))                        # returns string on a new line
    amount = float(line.rstrip('\n'))               # stores and makes value a float
    total += amount                                 # storage and calculation
    numbers = numbers + 1

average = total / numbers

print('The average is: ', average)

infile.close()                                      # close file

# Travis McDaniel
# 12/10/2020
# This program

# Create a text file named names.txt containing a series of names (as strings). The text file must be saved
# in this assignment's Python folder and submitted with the python program (.py) file.
# Write a program that displays the number (6,5,7 etc) of names that are stored in the file.
# (Hint: Open the file and read every string stored in it.
# Use a variable to keep a count of the number of items that are read from the file.)

infile = open('names.txt', 'r')                     # open the numbers file for reading
Counter = 0

names = infile.read()
family = names.split()

for members in family:                              # for loop and gets numbers in file
    print(members.rstrip())                     # returns string on a new line
    if members:                                     # if statement to store and calculate sum
        Counter += 1

print('There are', Counter, 'FamilyGuy members.')       # print statement with counter

infile.close()                                       # close file

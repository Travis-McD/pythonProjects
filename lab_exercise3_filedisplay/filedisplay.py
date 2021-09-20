# Travis McDaniel
# 12/10/2020
# This program (see below)
# Creates a text file named display.txt containing at least ten (10) U.S States (as strings).
# The text file must be saved in this assignment's Python folder and submitted with the python program (.py) file.
# Write a program that asks the user for the name of a file.
# The program should display only the first five lines of the file’s contents (States).


filename = input('Enter a filename: ')                  # get the name of file

try:                                        # use exceptions to handle errors (like  if: else: statement)
    infile = open(filename, 'r')            # open file
    state1 = infile.readline()              # read line in file
    state2 = infile.readline()              # "
    state3 = infile.readline()              # "
    state4 = infile.readline()              # "
    state5 = infile.readline()              # "
    print('These are the first five States in the display.txt file:')  # for info of contents
    print(state1, state2, state3, state4, state5)                      # print first 5 states
    infile.close()                                             # close file
except:                                                        # handle errors
    print('An ERROR occurred trying to read the file', filename)

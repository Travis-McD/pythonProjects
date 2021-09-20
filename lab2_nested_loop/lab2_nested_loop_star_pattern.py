# a program that prints a pattern of stars in descending order

# Name: Travis McDaniel
# Date: 11/4/2020

# Write a program that uses nested loops to draw this pattern:

#  *******
#  ******
#  *****
#  ****
#  ***
#  **
#  *
# print in 7 rows 7 columns using asterisk in iterations descending order using nested loop
# end operator from playback video Oct23 01:11:05

# declare vars

for row in range(7, 0, -1):
    for column in range(row, 0, -1):
        print('*', end='')  # all on one line
    print()  # this is needed to print a new line

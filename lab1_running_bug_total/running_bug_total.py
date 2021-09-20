# a program to take a sum per day and add up for a total

# Name: Travis McDaniel
# Date: 11/4/2020

# A bug collector collects bugs every day for five days.
# Write a program that keeps a running total of the number of bugs collected during the five days.
# The loop should ask for the number of bugs collected for each day, and when the loop is finished,
# the program should display the total number of bugs collected.

# declare vars
totalDays = 5
totalBugs = 0   # accumulator variable

# loop 5 times and ask for bugs collected each day
for eachDay in range(1, totalDays + 1):  # start with 1 and go five more
    bugCount = int(input("How many bugs did you catch on this day? Day" + str(eachDay) + ": "))  # prompt/function
    totalBugs += bugCount  # totalBugs = totalBugs + bugCount

# calculate and print total
print('----------------------------------------------')  # just for looks
print('Congrats! You have collected', totalBugs, 'bugs in', totalDays, 'Days')

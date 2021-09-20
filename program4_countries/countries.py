# Travis McDaniel
# 12/05/2020
# This program asks for 5 random capitals of countries and keeps count of correct and wrong's

# Write a program that creates a dictionary containing 20 countries as keys, and their capitals as values.
# (Use the Internet to get a list of countries and their capitals.)
# The program should then randomly quiz the user by displaying the name of a country
# (randomly generate/select the country) and asking the user to enter the capital
# The program should keep a count of the number of correct and incorrect responses.

import random                       # import random to use method on turn at line 37

country = {'Austria': 'Vienna',     # dictionary of countries as keys and capitals as values
           'Belgium': 'Brussels',
           'Brazil': 'Brasilia',
           'Canada': 'Ottawa',
           'China': 'Beijing',
           'Denmark': 'Copenhagen',
           'Egypt': 'Cairo',
           'Finland': 'Helsinki',
           'France': 'Paris',
           'Germany': 'Berlin',
           'Greece': 'Athens',
           'Hungary': 'Budapest',
           'Ireland': 'Dublin',
           'Italy': 'Rome',
           'Japan': 'Tokyo',
           'Mexico': 'Mexico City',
           'Russia': 'Moscow',
           'Spain': 'Madrid',
           'South Korea': 'Seoul',
           'Turkey': 'Ankara'}

correct = 0             # declared variables
wrong = 0
turn = 1
while turn <= 20:            # while loop to set condition using random.choice to ask for 5 capitals
    countries = random.choice(list(country))
    answer = input("What is the capital of " + countries + ": ")

    if answer == country[countries]:            # if else statements to
        correct += 1
    else:
        wrong += 1

    turn += 1
print("Correct answer: " + str(correct))        # print statement to display and calculate correct and wrong totals
print("Wrong answer: " + str(wrong))

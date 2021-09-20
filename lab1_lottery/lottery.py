# This program generate random lottery numbers
# Travis McDaniel
# 11/21/2020
# Design a program that generates seven lottery numbers.
#
# *The program should generate seven random numbers,
#
# each in the range of 0 through 9 and assign each number to a list element.
#
# *Then write another loop that displays the contents of the list.


import random       # needed for random module


def random_generator():  # a function to get 1 random number
    random_number = random.randint(0, 9)  # random.randint to get start and stop of a number
    return random_number                    # return for any function to call


def lottery_generator(number_of_lottery_numbers):        # function to get lottery numbers
    lottery_numbers = []                                 # empty list

    for number_index in range(7):            # for loop to iterate 7 times
        some_number = random_generator()     # variable to store func and call the func gen_rate_num
        lottery_numbers.append(some_number)  # append number to list

    return lottery_numbers                   # return for any function to call


def printer(lottery_list):   # func to display list of numbers/parameter list name(lottery_list)
    for number_index in range(len(lottery_list)):           # loop through list and display number stored in it
        print(lottery_list[number_index])   # print out number in list


def main():                                 # main function to call other functions/starting point
    digits = 7                              # numbers (constant variable)

    lottery_numbers = lottery_generator(digits)     # how many numbers to generate
    printer(lottery_numbers)                        # prints 7 random generated numbers in a list


main()                                              # call main function

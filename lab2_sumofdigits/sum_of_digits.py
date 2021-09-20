# This program prompts user for series of numbers and displays them added up
# Name: Travis McDaniel
# Date: 11/16/2020

# Write a program that asks the user to enter a series of single-digit
# numbers with nothing separating them

# The program should display the sum of all the
# single-digit numbers in the string.

# For example, if the user enters 2514, the program should output 12,
# which is the sum of 2, 5, 1, and 4.


def get_sum(user_number):                                                       # function with a loop to
    sum_of_digits = 0

    for stringy_digit in user_number:                                           # convert string too number
        inty_digit = int(stringy_digit)
        sum_of_digits = sum_of_digits + inty_digit

    return sum_of_digits


def main():                                                                     # function to control get_sum and print
    user_number = input("Please enter a series of single digit numbers with nothing separating them: ")

    sum_of_digits = get_sum(user_number)
    print("The sum of the digits in", user_number, "is: ", sum_of_digits)       # print string calculation


main()                                                                          # call to start program

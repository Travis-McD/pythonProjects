# This program calculates feet to inches
# Name: Travis McDaniel
# Date: 11/10/2020

# 1. Write a value returning function named max that accepts two integer values as arguments and returns
# the value that is the greater of the two. For example, if 7 and 12 are passed as arguments to the
# function, the function should return 12.
#
# 2. Use the function in a program that prompts the user to enter two integer values.
#
# 3. The program should display the value that is the greater of the two.

def max(first_number, second_number):       # custom value return function
    if first_number > second_number:        # if else statement to determine greater number
        return first_number
    else:
        return second_number


def get_number():
    user_first_number = int(input('Enter your first number: '))     # custom value return function
    user_second_number = int(input('Enter your second number: '))
    return user_first_number, user_second_number


def greater_number():                                                         # void function
    user_first_number, user_second_number = get_number()            # store return statement
    print('The greater number is', max(user_first_number, user_second_number))


greater_number()                                                              # call

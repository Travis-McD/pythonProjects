# This program calculates feet to inches
# Name: Travis McDaniel
# Date: 11/9/2020

# One foot equals 12 inches.

# Write a value returning function named feet_to_inches that accepts
# a number of feet as an argument and returns the number of inches in that many feet.

# Use the  feet_to_inches function in a program that prompts the user to enter:

# a number of feet then displays the number of inches in that many feet.

def feet_to_inches(userfeet):               # custom value return function defining feet_to_inches
    inches = userfeet * 12
    return inches                           # return statement


def func_convert():                                        # void function prompt user for amount
    user_amount = float(input('How many feet? '))
    inches = feet_to_inches(user_amount)                    # store return statement
    print('----------------------------------')             # just for style
    print('foot/feet               inches')                 # just for style
    print('----------------------------------')             # just for style
    print('  ', user_amount, '                 ', inches)   # print value


func_convert()                                              # call

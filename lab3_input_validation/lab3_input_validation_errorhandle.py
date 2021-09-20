# a program that prevents a input validation from being negative

# Name: Travis McDaniel
# Date: 11/4/2020

# John owns an import business, and he calculates the retail prices of her products with the following formula:

# retail Price = wholesale Cost × 2.5

# This program calculates retail prices.

MARK_UP = 2.5  # The markup percentage
another = 'y'  # Variable to control the loop.

# Process one or more items.
while another == 'y' or another == 'Y':
    wholesale = float(input("Enter the item's wholesale cost: "))
    retail = wholesale * MARK_UP
    if wholesale < 0:                                  # if statement to set wholesale to positive numbers only
        print('ERROR! The price can not be negative')  # warn user to not use negative numbers
    if wholesale > 0:                                  # re-write positive mark up
        print("Retail price:$", retail)

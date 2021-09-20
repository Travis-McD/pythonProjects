# This program generates 20 random numbers, 1 to 1000, then prompts user to choose one and determines if even or odd
# Name: Travis McDaniel
# Date: 11/11/2020

# 1. Write a value returning function named isEven that that accepts a random number as an argument and determines if
# the random number is even or odd. See the boolean section in Chapter 6- Fruitful functions

# 2. Use the function in a program that generates 20 random numbers between 1 and 1000.

# 3. The program should display if the random number generated is even or odd.

import random                                               # imported from local lib. to create generator


def generate_number():                                      # return function to get random number in a specific range
    random_number = random.randint(1, 1000)                 # module to generate random number
    return random_number                                    # return statement


def is_even(number):                                        # Boolean Function to test true or false
    if(number % 2) == 0:
        return True                                         # return statement for true
    if not(number % 2) == 0:
        return False                                        # multiple return statement for false


def calculate():                                            # function to prompt user and determine if odd or even
    print('These are your generated numbers')
    print('------------------------------------------------------------')

    def num():
        numb = int(input("Choose a Randomly Generated Number from above: "))
        if(numb % 2) == 0:                                  # if else statement to determine odd or even
            print(numb, "is a Even number")
        else:
            print(numb, "is a Odd number")

    num()                                                   # call def num(): function


def main():                                                 # conditional function listing numbers and loop
    even = 0

    for random_generator in range(1, 20):                   # for loop using range
        random_number = generate_number()
        print(random_number)
        if is_even(random_number):                          # if is even to decide even or odd
            even = even + 1                                 # could also use short version even =+ 1

    calculate()                                             # call from def calculate(): function


main()

print('------------------------------------------------------------')

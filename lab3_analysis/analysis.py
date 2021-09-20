# This program takes 20 random numbers from user and analyzes the numbers
# Travis McDaniel
# 11/24/2020
# Using the Lists operations, methods, and functions discussed in class,
# design a program that asks the user to enter a series of 20 numbers.
# The program should store the numbers in a list then display the following data:
# The lowest number in the list
# The highest number in the list
# The total of the numbers in the list
# The average of the numbers in the list


def get_values():       # function to make lists and loop for input and value
    # list for storage
    values = []
    # for loop using in operator and range function to prompt user
    for value in range(20):
        # variable to prompt user for a number 20 times
        value = (int(input("Enter A Random Number " + str(value + 1) + ": ")))
        # method that attaches values to list
        values.append(value)
    print('Please Enter 20 Random Numbers')
    return values


def analyze(numbers):          # function to get numbers and calculate using min max sum and then prints
    print("Lowest Number is:",  min(numbers))
    print("Highest Number is:", max(numbers))
    print("Sum The Numbers is:", sum(numbers))
    print("The Average The Numbers Is:", sum(numbers) / len(numbers))


def main():             # function to control all functions and runs program
    # variable that calls get_values function
    numbers = get_values()
    # calls analyze function and gets numbers
    analyze(numbers)


main()

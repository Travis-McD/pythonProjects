# This program prompts user for name and displays initials
# Name: Travis McDaniel
# Date: 11/16/2020

# Write a program that gets a string containing a person’s first, middle,
# and last names, and displays their first, middle, and last initials.
# For example, if the user enters John William Smith,
# the program should display J W S


def person_name():                                      # function to input string for names then store its value
    first_name = input("What is your first name: ")
    middle_name = input("What is your middle name: ")
    last_name = input("What is your last name: ")

    return first_name, middle_name, last_name


def get_initials(first_name, middle_name, last_name):   # this function allows me to store two values and
    first_initial = first_name[0]                       # find the index then make the index that character
    middle_initial = middle_name[0]
    last_initial = last_name[0]

    return first_initial, middle_initial, last_initial


def display_initials(first_initial, middle_initial, last_initial):      # function to print get_initials
    print(first_initial, middle_initial, last_initial)


def main():                                                             # the main function being controlled by the
    first_name, middle_name, last_name = person_name()                  # other functions
    first_initial, middle_initial, last_initial = get_initials(first_name, middle_name, last_name)

    display_initials(first_initial, middle_initial, last_initial)


main()                                                                  # call to start the program

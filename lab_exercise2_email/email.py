# Travis McDaniel
# 12/05/2020
# This is a program that creates a menu and gives user choices for name and email --used class video for birthdays

# Using the Dictionaries concepts and methods discussed in class,
#
# Write a program that keeps names and email addresses in a dictionary as key-value pairs.
#
# The program should display a menu that lets the user look up a person’s email address,
# add a new name and email address, change an existing email address, and delete an existing name and email address.

# global constants for menu

SEARCH = 1
ADD = 2
CHANGE = 3
DELETE = 4
STOP = 5


def main():     # function for empty dictionary
    emails = {}
    choice = 0

    while choice != STOP:       # loop to calculate menu choice
        choice = get_menu_choice()
        if choice == SEARCH:
            search(emails)
        elif choice == ADD:
            add(emails)
        elif choice == CHANGE:
            change(emails)
        elif choice == DELETE:
            delete(emails)


def add(emails):        # function to add new name and email
    name = input('Enter Name: ')
    email = input('Enter Email: ')
    # check if the name does not exist add it to dictionary
    if name not in emails:
        emails[name] = email
    else:
        print('That name already exists.')


def search(emails):     # function that searches name
    name = input('Enter Name: ')
    print(emails.get(name, 'Not found,'))


def change(emails):     # function to change email
    name = input('Enter Name: ')
    # check if the name does not exist and changes in dictionary
    if name in emails:
        email = input('Enter New Email: ')
        emails[name] = email
    else:
        print('This name is not found.')


def delete(emails):     # function to delete email
    name = input('Enter Name: ')
    # check if the name exists and deletes in dictionary
    if name in emails:
        del emails[name]
    else:
        print('That name is not found.')


def get_menu_choice():      # function to print menu choices and add style
    print()
    print('Contacts and their Emails')
    print('-------------------------')
    print('1. Search Email')
    print('2. Add Email')
    print('3. Change Email')
    print('4. Delete Email')
    print('5. Stop Program')

    choice = int(input('Enter your choice: '))
    # to check for search or stop choices and validates input
    while choice < SEARCH or choice > STOP:
        choice = int(input('Enter a valid choice: '))
    return choice


main()

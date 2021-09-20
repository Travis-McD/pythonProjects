# This program takes a string(movie title) and displays the first letter indexed of all the words in uppercase
# Name: Travis McDaniel
# Date: 11/16/2020

# Write a program that prompts the user for a string.
#
# The program should capitalize the first character of each word.
#
# For instance, if the user enters “hello my name is joe", the program should print the string “Hello My Name Is Joe"
# The modified string should be displayed. (hint: string splitting, slicing,  concatenation,  methods, etc)

def solve(capital):                                  # function using title method
    return capital.title()                           # take argument and change first letter in all words


def main():                                          # main function prompting user for input and storing variable
    capital = input("Please enter a title of a movie in all lower case letters: ")
    print(solve(capital))                            # print movie title but use solve function to change first letter


main()                                                 # call

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# def print_hi(name):
# Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# high_score = 95

# test1 = int(input("Enter the score for test 1: "))
# test2 = int(input("Enter the score for test 2: "))
# test3 = int(input("Enter the score for test 3: "))

# average = (test1 + test2 + test3) / 3

# print("The average score is ", average)

# if average >= high_score:
#    print("Congratulations")
#    print("That is a great average!")

# if elif else statement

# light = "yellow"

# if light == "green":
#    print("go")

# elif light == "yellow":
#    print("caution")

# else:
#    print("stop")

# program requests the exam score and prints the corresponding grade

# score = int(input("Enter your score: "))
# if score >= 90:
#     print("Your grade is A. ")
# elif score >= 80:
#     print("Your grade is B. ")
# elif score >= 70:
#     print("Your grade is C. ")
# elif score >= 60:
#     print("Your grade is D. ")
# elif score >= 50:
#     print("Your grade is F. ")
# else:
#     print("Invalid score")

# Using a for loop, write a program that prints any word/name 4 times

# for x in ["Travis", "Travis", "Travis", "Travis"]:
#     print(x)

# LISTS LISTS LISTS LISTS LISTS LISTS LISTS LISTS LISTS LISTS

# letters = ["a", "b", "c"]
# matrix = [[0,1], [2,3]]
# zeros = [0] * 100
# print(letters)

# letters = ["a", "b", "c"]
# matrix = [[0,1], [2,3]]
# zeros = [0] * 5
# combined = zeros + letters

# print(combined)

# Different type of list with range

# list(range(20))
# chars = list("Hello World")
# print(chars)


# LEN LEN LEN LEN LEN LEN LEN LEN LEN LEN LEN LEN LEN LEN

# letters = ["a", "b", "c"]
# matrix = [[0,1], [2,3]]
# zeros = [0] * 5
# combined = zeros + letters
# list(range(20))
# chars = list("Hello World")
# print(len(chars)

# How to access individual item in the list


# letters = ["a", "b", "c"]


# letters.append("d")                       # these are different methods you can remove has tags to check each one
# letters.insert(0, "-")
# letters.pop(1)
# print(letters)
# print(letters.count("d"))
# if "d" in letters:                                        # if statement to check if it exists first then run program
# print(letters.index("d"))
# print(letters.index("d"))                  # used to find a item in a list

# values = [2] * 5
# print(values)


# year = []
# jan = float(input('Please enter Jan rainfall: '))
# feb = float(input('Please enter Feb rainfall: '))
# mar = float(input('Please enter Mar rainfall: '))
# apr = float(input('Please enter Apr rainfall: '))
# may = float(input('Please enter May rainfall: '))
# jun = float(input('Please enter Jun rainfall: '))
# jul = float(input('Please enter Jul rainfall: '))
# aug = float(input('Please enter Aug rainfall: '))
# sep = float(input('Please enter Sep rainfall: '))
# oct = float(input('Please enter Oct rainfall: '))
# nov = float(input('Please enter Nov rainfall: '))
# dec = float(input('Please enter Dec rainfall: '))
#
# year.extend((jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec))
#
#
# def lowest():
#     print('The minimum rainfall is', min(year))
# lowest()
#
#
# def highest():
#     print('The most rainfall is', max(year))
# highest()
#
#
# def total():
#     print('The total rainfall is', sum(year))
# total()
#
#
# def average():
#     print('The average rainfall is', float(sum(year))/len(year))
# average()

import random

states = {
    "Alabama": "Montgomery",
    "California": "Sacramento",
    "Florida": "Tallahassee",
    "Hawaii": "Honolulu",
    "Indiana": "Indianapolis",
    "Michigan": "Lansing",
    "New York": "Albany",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Wisconsin": "Madison"
}
correct = 0
wrong = 0
turn = 1
while turn <= 5:
    current_state = random.choice(list(states))
    answer = input("What is the capital of " + current_state + ": ")

    if answer == states[current_state]:
        correct += 1
    else:
        wrong += 1

    turn += 1
print("Correct answer: " + str(correct))
print("Wrong answer: " + str(wrong))

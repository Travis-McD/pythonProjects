# This program takes 5 averages and displays there grade
# Name: Travis McDaniel
# Date: 11/13/2020

# Write a program that asks the user to enter five test scores.

# The program should display a letter grade for each score and the average test score.

# Write the following functions in the program:

# calc_average. This function should accept five test scores as arguments and return the average of the scores.

# determine_grade. This function should accept a test score as an argument and return
# a letter grade for the score based on the following grading scale:

# Score	Letter Grade
# 90–100	A
# 80–89	    B
# 70–79	    C
# 60–69	    D
# Below 60	F

def calc_average(score1, score2, score3, score4, score5):   # function that calculates the average score to grade
    average = (score1 + score2 + score3 + score4 + score5) / 5
    return average


def determine_grade(user_score):                    # function that has a if,elif statement  for user score
    if user_score < 60:                             # and returns a grade
        return 'F'
    elif user_score < 70:
        return 'D'
    elif user_score < 80:
        return 'C'
    elif user_score < 90:
        return 'B'
    elif user_score < 101:
        return 'A'


def ask_for_scores():                                   # function to prompt user for score and store value
    score1 = float(input('Enter Score 1: '))            # convert str to float and prompt user for score
    score2 = float(input('Enter Score 2: '))
    score3 = float(input('Enter Score 3: '))
    score4 = float(input('Enter Score 4: '))
    score5 = float(input('Enter Score 5: '))

    return score1, score2, score3, score4, score5


def print_diagram(score1, score2, score3, score4, score5):      # function to print
    print('-----------------------')
    print('Score     Letter Grade  ')
    print('-----------------------')
    print(str(score1) + '          ' + determine_grade(score1))
    print(str(score2) + '          ' + determine_grade(score2))
    print(str(score3) + '          ' + determine_grade(score3))
    print(str(score4) + '          ' + determine_grade(score4))
    print(str(score5) + '          ' + determine_grade(score5))


def main():                                                         # function to display results
    score1, score2, score3, score4, score5 = ask_for_scores()
    print_diagram(score1, score2, score3, score4, score5)


main()                                                              # call

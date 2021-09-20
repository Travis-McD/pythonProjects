# Travis McDaniel
# 12/4/2020
# This is a program using dictionaries to display Course information

# Using the Dictionaries concepts and methods discussed in class,
# Write a program that creates a dictionary containing course numbers and
# the room numbers of the rooms where the courses
# meet. The dictionary should have the following key-value pairs:
# Course Number (key)	Room Number (value)
# ITP100	3004
# ITP200	4501
# CSC101	6755
# CSC102	1244
# CSC103	1411
# The program should also create a dictionary containing course numbers and
# the names of the instructors that teach each
# course. The dictionary should have the following key-value pairs:
# Course Number (key)	Instructor (value)
# ITP100	Addy
# ITP200	Carter
# CSC101	Rich
# CSC102	Burke
# CSC103	Lee
# The program should also create a dictionary containing course numbers and
# the meeting times of each course.
# The dictionary should have the following key-value pairs:
# Course Number (key)	Meeting Time (value)
# ITP100	8:00 a.m.
# ITP200	9:00 a.m.
# CSC101	10:00 a.m.
# CSC102	11:00 a.m.
# CSC103	1:00 p.m.
# * The program should let the user enter a course number, then it should display
# the course’s room number, instructor, and meeting time.

# first dictionary with course number as a key and room numbers as values
roomNumber = {'ITP100': '3004',
              'ITP200': '4501',
              'CSC101': '6755',
              'CSC102': '1244',
              'CSC103': '1411'}

# secon dictionary with course number as a key and instructors names as values
instructorName = {'ITP100': 'Addy',
                  'ITP200': 'Carter',
                  'CSC101': 'Rich',
                  'CSC102': 'Burke',
                  'CSC103': 'Lee'}

# Third dictionary with course number as a key and course times as values
courseTime = {'ITP100': '8:00 a.m.',
              'ITP200': '9:00 a.m.',
              'CSC101': '10:00 a.m.',
              'CSC102': '11:00 a.m.',
              'CSC103': '1:00 p.m.'}

# used to print the keys in first dictionary used to display course numbers
for key in roomNumber.keys():
    print(key)

print('-------------------------------------------------------')

# prompt user for input of course number
courseNumber = input('Please choose a course number from above for more info: ')

# if else statement to check for course number and print info or whether the course number is valid
if courseNumber in roomNumber:
    print()
    print('Room Number:   ', roomNumber[courseNumber])
    print('Instructor:    ', instructorName[courseNumber])
    print('Course Time:  ', courseTime[courseNumber])
else:
    print('Invalid course number.')

# This program calculates the distance a vehicle travels
# Name: Travis McDaniel
# Date: 11/6/2020

# The distance a vehicle travels can be calculated as follows:

#                      distance = speed × time
# For example, if a train travels 40 miles per hour for three hours, the distance traveled is 120 miles.
# *Write a program that asks the user for the speed of a vehicle (in miles per hour) and the number of hours it has
# traveled.

# *How can you tell when a user has input invalid data?

# Add while statements to check if the user has entered something other than a number and "perform appropriate action".
# (You could ask them for another number)
# *It should then use a loop to display the distance the vehicle has traveled for each hour of that time period.

another = 'y'  # Variable to control the loop.

while another == 'y' or another == 'Y':
    vehicleSpeed = float(input(' What is the speed of the vehicle?  '))
    retail = wholesale * MARK_UP
    if wholesale < 0:
        print('ERROR! the number must be whole')
    if wholesale > 0:
        print("Retail price:$", retail)

timeTraveled = float(input('How many hours has it traveled?  '))
while timeTraveled <= 0:
    print('Please enter a positive number for time travelled speed')
    timeTraveled = float(input('How many hours has it traveled?  '))


print('Hour', '     Distance Traveled')
print('---------------------------')
for thisHour in range(1, timeTraveled + 1):
    distTraveled = vehicleSpeed * thisHour
    print(thisHour, '       ', distTraveled)

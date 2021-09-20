# This program is for the calculation of weight and mass

# Travis McDaniel
# 10/25/2020

# Scientists measure an object’s mass in kilograms and its weight in newtons.
# If you know the amount of mass of an object in kilograms, you can calculate
# its weight in newtons with the following formula:
# weight = mass * 9.8
# Write a program that asks the user to enter an object’s mass, then calculates its weight.
# If the object weighs more than 500 newtons, display a message indicating that it is too heavy.
# If the object weighs less than 100 newtons, display a message indicating that it is too light.

# prompt user for an objects mass
userObject = float(input('Enter a object Mass in kilograms: '))

# Determine mass calculations:
if userObject > 500:
    print('Your Object is too heavy!')
elif userObject < 100:
    print('Your Object is too light!')
else:
    print(userObject * 9.8, 'newtons')

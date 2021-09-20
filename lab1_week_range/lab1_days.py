# This program will prompt user for a number 1-7
# then print the day of week its equal to

# Travis McDaniel
# 10/24/2020

# Get a number 1-7 from user
userNumber = int(input('Enter a number in the range of 1-7: '))

# Determine the day.
if userNumber == 1:
    print('Monday')
elif userNumber == 2:
    print('Tuesday')
elif userNumber == 3:
    print('Wednesday')
elif userNumber == 4:
    print('Thursday')
elif userNumber == 5:
    print('Friday')
elif userNumber == 6:
    print('Saturday')
elif userNumber == 7:
    print('Sunday')
else:
    print('ERROR! Please rerun program and enter a number 1-7')

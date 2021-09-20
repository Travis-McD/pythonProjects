# This is a program to calculate the salary
# programmed by Travis McDaniel
# 10/14/2020

# input values (step 1)
firstName = input("What is your first name? ")
firstName = str(firstName)

middleInitial = input("What is your middle initial, please press space bar if none? ")
middleInitial = str(middleInitial)

lastName = input("What is your last name? ")
lastName = str(lastName)

hoursEarned = input("How many hours did you earn this period? ")
hoursEarned = float(hoursEarned)

hourlyRate = input("What is your base hourly pay? ")
hourlyRate = float(hourlyRate)

# calculate salary (step 2)
associate = lastName + " " + firstName + " " + middleInitial + "."
associate = str(associate)

grossSalary = hoursEarned * hourlyRate
grossSalary = float(grossSalary)

# Output results
print("Associate: ", associate)
print("Gross Base Pay this period: ", "$", grossSalary)


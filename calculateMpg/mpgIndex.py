# This is a program to calculate the MPG on a trip
# programmed by Travis McDaniel
# 10/15/2020

# input values (step 1 and 2)
firstName = input("What is your first name? ")
firstName = str(firstName)

lastName = input("What is your last name? ")
lastName = str(lastName)

tripMiles = input("How many miles on your trip? ")
tripMiles = float(tripMiles)

tripGallons = input("How many Gallons did you use? ")
tripGallons = float(tripGallons)

tripLiters = tripGallons

tripKm = tripMiles

# Calculate Algorithm (step 3)
autoOwner = lastName + " " + firstName + " "

tripMpg = tripMiles / tripGallons

tripMetric = 235 / tripMpg

# Output results (step 4)
print("Auto Owner: ", autoOwner)

# standard conversion
print("Trip MPG average: ", tripMpg)

# metric conversion
print("Trip L/100KM average: ", tripMetric)

# This program
# Travis McDaniel
# 11/23/2020
# Using the Lists operations, methods, and functions discussed in class,
# design a program that lets the user enter the total rainfall for each of
# the 12 months into a list.
#
# The program should calculate and display the total rainfall for the year,
#
# the average monthly rainfall, the months with the highest and lowest amounts.


def rainfall_amounts(names_of_months):      # function to receive a list of months parameter names_of_months

    # variable for amount of months
    months_in_year = 12

    # List to store total
    total_rainfall_list = []

    # loop to prompt user for amount and create a list of 12
    for current_month_index in range(months_in_year):

        # variable assigning names to 12 elements in list using a float variable
        monthly_rainfall = float(input("Enter Rainfall for "
                                       + names_of_months[current_month_index] + ": "))

        # link monthly_rainfall to list
        total_rainfall_list.append(monthly_rainfall)
    return total_rainfall_list


def calculate_rainfall(total_rainfall_list):      # function to calculate total rainfall
    # List to store total
    total_rainfall = 0

    # loop through list that adds up
    for current_monthly_rainfall_index in range(len(total_rainfall_list)):

        # variable to calculate total rainfall by adding
        total_rainfall = total_rainfall + total_rainfall_list[current_monthly_rainfall_index]
    return total_rainfall


def average_month(total_rainfall_list):    # function to calculate monthly average

    # variable that gets number of month from list (12)
    number_of_months = len(total_rainfall_list)

    # variable to calculate average dividing number of months
    average_rainfall = calculate_rainfall(total_rainfall_list) / number_of_months
    return average_rainfall


def highest_month(total_rainfall_list, names_of_months):  # function to find highest month

    # variable with max function to get highest on list using index to get elements
    highest_rainfall_amount = max(total_rainfall_list)

    # variable to call index function and index highest amount 0-11
    highest_rainfall_amount_index = total_rainfall_list.index(highest_rainfall_amount)
    return names_of_months[highest_rainfall_amount_index]


def lowest_month(total_rainfall_list, names_of_months):   # function to find lowest month

    # variable with max function to get lowest on list using index to get elements
    lowest_rainfall_amount = min(total_rainfall_list)

    # variable to call index function and index lowest amount 0-11
    lowest_rainfall_amount_index = total_rainfall_list.index(lowest_rainfall_amount)
    return names_of_months[lowest_rainfall_amount_index]


def print_rainfall_statistics(total_rainfall_list, names_of_months, total_rainfall, average_rainfall,  # print function
                              highest_rainfall_month, lowest_rainfall_month):                         # what to display

    # for loop to go through names/lists, calculate and print total, average, highest and lowest
    for current_month_index in range(len(names_of_months)):
        print(names_of_months[current_month_index], total_rainfall_list[current_month_index])
    print("Total Rainfall: " + str(total_rainfall),
          "Average Rainfall: " + str(average_rainfall),
          highest_rainfall_month + "has the highest rainfall",
          lowest_rainfall_month + "has the lowest rainfall",)


def main():                                             # function to call other functions and run program
    # List to store total names
    names_of_months = ["January ", "February ", "March ", "April ", "May ", "June ", "July ",
                       "August ", "September ", "October ", "November ", "December "]

    # List to store total
    total_list = []

    # variable that gets month amounts and names
    total_rainfall_list = rainfall_amounts(names_of_months)

    # variable that calls calculate_rainfall function passes total_rainfall list
    total_rainfall = calculate_rainfall(total_rainfall_list)

    # variable that calls the average_month functions passes total_rainfall list
    average_monthly_rainfall = average_month(total_rainfall_list)

    # variable that calls the highest_month functions passes total_rainfall list and name of months
    highest_rainfall_month = highest_month(total_rainfall_list, names_of_months)

    # variable that calls the lowest_month functions passes total_rainfall list and name of months
    lowest_rainfall_month = lowest_month(total_rainfall_list, names_of_months)

    print_rainfall_statistics(total_rainfall_list, names_of_months, total_rainfall,
                              average_monthly_rainfall, highest_rainfall_month, lowest_rainfall_month)


main()

# Samuel Foss
# Program 3: Tax Rate
# 10/11/2024
from random import setstate


# Program #3: Tax Rate
# A retail company must file a monthly sales tax report listing the total sales for the month,
# and the amount of state and county sales tax collected.
# The state sales tax rate is 5 percent and the county sales tax rate is 2.5 percent.
# Write a program that asks the user to enter the total sales for the month.
# From this figure, the application should calculate and display the following:

# The amount of county sales tax.
# The amount of state sales tax.
# The total sales tax (county plus state)
# Use at least one function with input and output in this program

def calculations(sales):
    statetax = 0.05 * sales
    countytax = 0.025 * sales
    totaltax = statetax + countytax
    return [statetax, countytax, totaltax]

salesreport = float(input("Enter the total sales of the month: $"))
taxes = calculations(salesreport)
print(f'State tax: ${taxes[0]:.2f}\nCounty tax: ${taxes[1]:.2f}\nTotal tax: ${taxes[2]:.2f}')

# Output
# Enter the total sales of the month: $105215
# State tax: $5260.75
# County tax: $2630.38
# Total tax: $7891.12

# Process finished with exit code 0

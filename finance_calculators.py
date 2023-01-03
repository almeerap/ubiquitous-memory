# a program that allows the user to access two different financial calculators
# an investment calculator and a home loan repayment calculator
# user will choose whether they want to use the investment or bond
# depending on option, user will have to input various information 
# in order for the total amount to be calculated successfully

import math

print("Please read the following: Investment - to calculate the amount of interest you'll earn on your investment. Bond - to calculate the amount you'll have to pay on a home loan")
calculation = input("Please enter in either 'investment' or 'bond' as your choice: ").lower()

if calculation == "investment":
    deposit = float(input("Please enter the amount of money you are depositing: "))
    interest_rate = float(input("Please enter the interest rate without '%' sign: "))
    num_years = float(input("Please enter the number of years you plan on investing: "))
    interest = input("Please enter the type of interest: simple or compound ").lower()
    new_ir = interest_rate / 100
    if interest == "simple":
     total_amount = deposit * (1 + new_ir * num_years)
     print(total_amount)
    else:
        total_amount = deposit * math.pow((1 + new_ir), num_years)
        print(round(total_amount, 2))

if calculation == "bond":
    house_value = float(input("Please enter the present value of the house: "))
    interest_rate2 = float(input("Please enter the interest rate without '%' sign: "))
    num_months = int(input("Please enter the number of months you plan to take to repay the bond: "))
    new_ir2 = interest_rate2 / 12
    total_amount = (house_value * (new_ir2 / 100)) / (1 - math.pow(1 + new_ir2, - num_months))
    print(round(total_amount, 2))

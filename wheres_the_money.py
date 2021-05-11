#
#Author: Dillon Barr
#Description: This program takes user financial inputs and prints out a 
#             table showing expenses, percents they represent and leftover or deficit money.
#


from os import _exit as exit

print("-" * 29)
print("----- WHERE'S THE MONEY -----")
print("-" * 29)


annualSalary = input("What is your annual salary?\n")
if annualSalary.isnumeric == False:
    print("Must enter positive integer number.")
    exit(0)
annualSalary = int(annualSalary)
if annualSalary < 0:
    print("Must enter positive integer number.")
    exit(0)
    
monthlyRent = input("How much is your monthly mortgage/rent?\n")
if monthlyRent.isnumeric == False:
    print("Must enter positive integer number.")
    exit(0)
monthlyRent = int(monthlyRent)
if monthlyRent < 0:
    print("Must enter positive integer number.")
    exit(0)
    
monthlyBills = input("What do you spend on bills monthly?\n")
if monthlyBills.isnumeric == False:
    print("Must enter positive integer number.")
    exit(0)
monthlyBills = int(monthlyBills)
if monthlyBills < 0:
    print("Must enter positive integer number.")
    exit(0)
    
weeklyFoodCost = input("What are your weekly grocery/food expenses?\n")
if weeklyFoodCost.isnumeric == False:
    print("Must enter positive integer number.")
    exit(0)
weeklyFoodCost = int(weeklyFoodCost)
if weeklyFoodCost < 0:
    print("Must enter positive integer number.")
    exit(0)
    
annualTravel = input("How much do you spend on travel annually?\n")
if annualTravel.isnumeric == False:
    print("Must enter positive integer number.")
    exit(0)
annualTravel = int(annualTravel)
if annualTravel < 0:
    print("Must enter positive integer number.")
    exit(0)
    
taxPercentage = input("Tax percentage?\n")
if taxPercentage.isnumeric == False:
    print("Must enter positive integer number.")
    exit(0)
taxPercentage = int(taxPercentage)
if taxPercentage < 0:
    print("Must enter positive integer number.")
    exit(0)
if taxPercentage > 100:
    print("Tax must be between 0% and 100%.")
    exit(0)
    
yearlyRent = monthlyRent * 12
yearlyBills = monthlyBills * 12
yearlyFoodCost = weeklyFoodCost * 52
tax = taxPercentage / 100
rentPercent = (yearlyRent / annualSalary) * 100
billPercent = (yearlyBills / annualSalary) * 100
foodPercent = (yearlyFoodCost / annualSalary) * 100
travelPercent = (annualTravel / annualSalary) * 100
taxWithheld = (annualSalary * tax)
extra = annualSalary - yearlyRent - yearlyBills - yearlyFoodCost - annualTravel - taxWithheld
extraPercent = (extra / annualSalary) * 100
dashes = max(int(rentPercent), int(billPercent), int(foodPercent), int(travelPercent), int(taxPercentage), int(extraPercent))

print("\n" + "-" * 41 + "-" * dashes)
print("See the financial breakdown below, based on a salary of $", 
    annualSalary, sep='')
print("-" * 41 + "-" * dashes)
print("| mortgage/rent | $", format(yearlyRent, '9,d'), "|", 
    format(rentPercent, '5,.1f') + "% | " + "#" * int(rentPercent))
print("|         bills | $", format(yearlyBills, '9,d'), "|", 
    format(billPercent, '5,.1f') + "% | " + "#" * int(billPercent))
print("|          food | $", format(yearlyFoodCost, '9,d'), "|",
    format(foodPercent, '5,.1f') + "% | " + "#" * int(foodPercent))
print("|        travel | $", format(annualTravel, '9,d'), "|", 
    format(travelPercent, '5,.1f') + "% | " + "#" * int(travelPercent))
print("|           tax | $", format(taxWithheld, '9,'), "|", 
    format(taxPercentage, '5,.1f') + "% | " + "#" * int(taxPercentage))
if extra > 0:
    print("|         extra | $", format(extra, '9,'), "|",
    format(extraPercent, '5,.1f') + "%" + " | " + "#" * int(extraPercent))
else:
    print("|         extra | $", format(extra, '9,'), "|",
    format(extraPercent, '5,.1f') + "% | ")
print("-" * 41 + "-" * dashes)
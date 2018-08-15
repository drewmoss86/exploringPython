# Andrew Moss
# Assignment 2 : Cash Register
# CS 002
from decimal import *
purAmt = float(input("Enter purchase amount: "))
recAmt = float(input("Enter received amount: "))

totalChange = recAmt*100 - purAmt*100

print("Total Change: $", totalChange/100)

dollars = int(totalChange/100)
print("dollars:", dollars)
totalChange -= dollars*100

if(totalChange/25 < 1):
    quarters = 0
else:
    quarters = int(totalChange/25)
print("quarters:", quarters)
totalChange -= quarters*25

if(totalChange/10 < 1):
    dimes = 0
else:
    dimes = int(totalChange/10)
print("dimes:", dimes)
totalChange -= dimes*10

if(totalChange/5 < 1):
    nickels = 0
else:
    nickels = int(totalChange/5)
print("nickels:", nickels)
totalChange -= nickels*5

if(totalChange/1 < 1):
    pennies = 0
else:
    pennies = int(totalChange/1)
print("pennies:", pennies)

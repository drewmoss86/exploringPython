# Andrew Moss
# CS 002 Lab 1 : Using Variables for math, input and output


ex = int(input("Please select the following exercise: "))

# This program will take integers and find the sum, differnece, product and quotient
if(ex == 1):
    int1 = int(input("Enter first value: "))
    int2 = int(input("Enter second value: "))
    add = int1 + int2
    diff = int1 - int2
    prod = int1 * int2
    quot = int1 / int2
    mod = int1 % int2
    print(int1, '+', int2, '=', add)
    print(int1, '-', int2, '=', diff)
    print(int1, '*', int2, '=', prod)
    print(int1, '/', int2, '=', quot)
    print(int1, '%', int2, '=', mod)
# This program will find the sum and average of six floating point values input by user
elif ex == 2:
    int1 = float(input("Enter six fp numbers on a single line, separated by spaces: "))
    int2 = float(input())
    int3 = float(input())
    int4 = float(input())
    int5 = float(input())
    int6 = float(input())
    array = {int1, int2, int3, int4, int5, int6}
    add = sum(array)
    avg = add / 6
    print("Sum of", int1, int2, int3, int4, int5, int6, "is", add)
    print("Avg = ", avg)
# This program will take user input age value and calculate a target heart rate
elif ex == 3:
    age = int(input("What is your age? "))
    ll = (220 - age) * .6
    ul = (220 - age) * .75
    print("Your target heart rate is between", ll, "and", ul, "bpm.")

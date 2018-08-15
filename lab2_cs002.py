# Andrew Moss
# Lab 2 : ISBN Checksum
# CS 002

# select exercise
ex = int(input("What exercise? "))
if(ex == 1):
    # prompt user for isbn value
    isbn = int(input("Please enter the first 9 digits of the ISBN: "))
    # calc weighted sum
    iter = 9
    wtSum = 0
    #loop to calc weighted sum
    while True:
        if(iter > 0):
            # starting last value working back
            val = isbn % 10
            # new isbn value
            isbn = int(isbn / 10)
            # add weight value to total weighted sum
            wtSum += val * iter
            # decrement iter by 1
            iter -= 1
        # when iter value is 0, exit loop
        else:
            break
    # calc checksum value
    checkSum = wtSum % 11
    print("CheckSum: ", checkSum)

elif(ex == 2):
    # prompt user for character (upper or lower)
    ch = input("Enter a character: ")
    # initialize pos variable to store char position
    pos = 0
    # if character is UPPER case
    if ord(ch) <= 90 and ord(ch) >= 65:
        pos = ord(ch) - ord('A') + 1
    # if character is LOWER case
    if ord(ch) <= 122 and ord(ch) >= 97:
        pos = ord(ch) - ord('a') + 1
    print(ch, "is letter", pos)

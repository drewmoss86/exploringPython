# Andrew Moss
# Lab 3 : Branching
# CS 002

def menu(*args):
    print("a. Go to the movies")
    print("b. Eat out")
    print("c. Hang out at the Mall")
    print("d. Go watch the Dodgers")

ex = int(input("Which exercise? "))

# Time calculator
if(ex == 1):
    # prompt user to input number of seconds
    sec = int(input("Enter a number of seconds: "))

    # one min
    if(sec >= 60 and sec < 120):
        print("There is", int(sec/60), "min in", sec, "seconds.")
    # multiple mins
    if(sec >= 120 and sec < 3600):
        print("There are", int(sec/60), "mins in", sec, "seconds.")
    # one hour
    if(sec >= 3600 and sec < 7200):
        print("There is", int(sec/3600), "hour in", sec, "seconds.")
    # multiple hours
    if(sec >= 7200 and sec < 86400):
        print("There are", int(sec/3600), "hours in", sec, "seconds.")
    # one day
    if(sec >= 86400 and sec < 172800):
        print("There is", int(sec/86400), "day in", sec, "seconds.")
    # multiple days
    if(sec >= 172800):
        print("There are", int(sec/86400), "days in", sec, "seconds.")

elif(ex == 2):
    menu()
    option = input("What do you want to do tonight? ")
    if(option == 'a' or option == 'A'):
        print("I know just the movie to see!")
    elif(option == 'b' or option == 'B'):
        print("Great! I’ve been wanting to try that new Tuvaluan restaurant!")
    elif(option == 'c' or option == 'C'):
        print("You bring the cash!")
    elif(option == 'd' or option == 'D'):
        print("Take me out to the ball game …")
    else:
        print("Nothing suits you, then? I guess we’ll just stay and program!")

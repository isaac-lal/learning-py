# freeCodeCamp.org: Learn Python - Full Course for Beginners [Tutorial] (3:04:18)

try:  # catches when the user does something wrong and executes except statement
    # answer = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err: # always specify except, no "except:"
    print(err)
except ValueError:
    print("Invalid Input")
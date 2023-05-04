# freeCodeCamp.org: Learn Python - Full Course for Beginners [Tutorial] (1:54:07)

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3: # when comparing, it returns a true or false value
        return num1
    elif num2 >= num1 and num2 >= num3: # same thing can be done with strings
        return num2
    else:
        return num3
    
# can also use ! (not equal), == (equal)

print(max_num(24, 72, 67))

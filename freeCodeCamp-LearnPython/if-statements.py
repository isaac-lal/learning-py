# freeCodeCamp.org: Learn Python - Full Course for Beginners [Tutorial] (1:40:06)

is_male = False
is_tall = True

if is_male:
    print("You are a male") # if false, doesn't print anything
else:
    print("You are not a male")

if is_male or is_tall: # one OR the other
    print("You are a male or tall or both")
else:
    print("You are neither male nor tall")

if is_male and is_tall: # includes both
    print("You are a tall male")
elif is_male and not(is_tall): # elif is else-if and it adds multiple if statements
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but tall")
else:
    print("You are either not male or not tall or both")
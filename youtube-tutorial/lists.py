# freeCodeCamp.org: Learn Python - Full Course for Beginners [Tutorial] (1:03:10)

friends = ["Sidrat", "Minal", "Dorothea", "Coby", "random"] # runs code of list one by one name
# index:       0        1          2         3        4

print(friends)
print(friends[3]) # references element of list by string
print(friends[-3]) # references elements from the back of the list (last element = -1)
print(friends[0:4]) # only grabs elements from the first element forward (stops at last value: 4 which is "random")

friends[-1] = "Other random" # changes element of the index (-1 is "random" which changes to "Other random")
print(friends[-1])
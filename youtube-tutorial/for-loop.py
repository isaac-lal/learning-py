# freeCodeCamp.org: Learn Python - Full Course for Beginners [Tutorial] (2:32:44)

for letter in "Hello, my name is Isaac": # prints all letters in string one by one
    print(letter)

friends = ["Sidrat", "Minal", "Dorothea", "Coby"]
for friend in friends: # prints all string values in array one by one
    print(friend)

for index in range(3, 10): # prints all numbers in range, not including last number
    print(index)

for index in range(len(friends)): # calculates elements of array and prints it out
    print(friends[index])

for index in range(5):
    if index == 0:
        print("First iteration")
    else:
        print("Not first")
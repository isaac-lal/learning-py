# freeCodeCamp.org: Learn Python - Full Course for Beginners [Tutorial] (1:10:44)

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]

# friends.extend(lucky_numbers) # extends list with another list
friends.append("Creed") # adds another into the end of the list
# friends.insert(1, "Kelly") # adds element in index position
friends.remove("Jim") # removes string from list
# friends.clear() # removes whole list
friends.pop() # removes last element of a list

friends.sort() # sorts list in alphabetical order
print(friends)
print(friends.index("Kevin")) # displays index where element is at
print(friends.count("Jim"))


# lucky_numbers.sort() # sorts numbers in ascending order
print(lucky_numbers)
lucky_numbers.reverse() # reverses order of list
print(lucky_numbers) 

friends2 = friends.copy() # copies the list that is referenced
print(friends2)
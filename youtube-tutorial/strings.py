# freeCodeCamp.org: Learn Python - Full Course for Beginners [Tutorial] (27:03)

print("Giraffe\nAcademy")
print("-------------------")

phrase = "Giraffe Academy"
print(phrase + " is cool") # Concatenation: combining strings/variables
print(phrase.lower()) # converts string to lowercase
print(phrase.upper()) # converts string to uppercase
print(phrase.isupper()) # returns false because not uppercase
print(phrase.upper().isupper()) # returns true because converts to uppercase
print(len(phrase)) # calculates number of characters in a string
print(phrase[0]) # grabs first character of a string (starts with a 0 index)
                 # example: Giraffe Academy
                 #          0123456789->
print(phrase[3])
print(phrase.index("G")) # returns index of string (0)
print(phrase.index("a"))
print(phrase.index("Acad")) # returns index of where phrase starts
print(phrase.replace("Giraffe", "Elephant")) # replace phrases/letters with other ones
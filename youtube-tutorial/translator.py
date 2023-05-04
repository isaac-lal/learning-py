# freeCodeCamp.org: Learn Python - Full Course for Beginners [Tutorial] (2:52:42)

def censor_vowels(phrase):
    censoring = ""
    
    for letter in phrase:
        if letter.lower in "aeiou":
            if letter.isupper():
                censoring += "*"
            else:
                censoring += "*"
            censoring += "*"
        else:
            censoring += letter
    
    return censoring

print(censor_vowels(input("Enter a phrase: ")))
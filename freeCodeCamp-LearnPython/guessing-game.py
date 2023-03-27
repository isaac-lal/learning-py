# freeCodeCamp.org: Learn Python - Full Course for Beginners [Tutorial] (2:20:01)

secret_word = "Yessir"
guess = ""
tries = 0
tries_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if tries < tries_limit: # as long as you have tries, the game continues
        guess = input("Guess the secret word: ")
        tries += 1
    else:
        out_of_guesses = True

if out_of_guesses: # if out_of_guesses is true then you lose
    print("Out of Guesses, YOU LOSE!")
else: 
    print("YOU WIN!")
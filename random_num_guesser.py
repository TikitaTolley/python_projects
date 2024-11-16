# generate a random number and guess how many times it takes for the user to guess this number

import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():         # makes sure input is digit (return True) before conversion into an integer
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()

else:
    print("Please type a number next time.")
    quit()


random_number = random.randint(0, top_of_range)       # (start, stop), randrange will not include 11

guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():          # makes sure input is digit (return True) before conversion into an integer
        user_guess = int(user_guess)

    else:
        print("Please type a number next time.")
        continue

    if user_guess == random_number:
        print("You got it right!")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in", guesses, "guesses")
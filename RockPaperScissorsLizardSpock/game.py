'''
As Sheldon explains, "Scissors cuts paper, paper covers rock, rock crushes lizard, 
lizard poisons Spock, Spock smashes scissors, scissors decapitates lizard, lizard eats paper, 
paper disproves Spock, Spock vaporizes rock, and as it always has, rock crushes scissors."

'''

import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors", "lizard", "spock"]

while True:
    user_input = input("Type Rock/Paper/Scissors/Lizard/Spock or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 4)        # rock: 0, paper: 1, scissors: 2, lizard: 3, spock: 4

    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    elif user_input == "rock" and computer_pick == "lizard":
        print("You won!")
        user_wins += 1

    elif user_input == "lizard" and computer_pick == "Spock":
        print("You won!")
        user_wins += 1

    elif user_input == "Spock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "lizard":
        print("You won!")
        user_wins += 1

    elif user_input == "lizard" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "Spock":
        print("You won!")
        user_wins += 1

    elif user_input == "Spock" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == computer_pick:
        print("Try again!")
        continue

    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")
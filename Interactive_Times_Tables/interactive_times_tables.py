import os
from time import sleep
import random

def ClearScreen():
    os.system('clear')


user_input = 0

while True:
    question_1 = input("Would you like to practice your times tables or dare to try the random multiplication game? (tt, rmg or q to quit) ").lower()    
    if question_1 == "tt":
        print("You chose Times Tables!")
        times_tables = input("Choose which times table you'd like to practice today? (1/2/3/4/5/6/7/8/9/10/11/12/13) ")
        while True:
            random_number = random.randint(0, 14)
            
            answer_1 = input("(q to quit) " + times_tables + " x " + str(random_number) + " = ").lower()
            if answer_1 == str(int(times_tables) * random_number):
                user_input += 1
                print("You got it right!")
                continue

            elif answer_1 == "q":
                break
            
            else:
                print("Better luck next time!")
                continue


        
    elif question_1 == "rmg":
        print("You chose the random multiplication game!")
        while True:
            rand_numb_1 = random.randint(0, 14)
            rand_numb_2 = random.randint(0, 14)

            answer_2 = input("(q to quit) " + str(rand_numb_1) + " x " + str(rand_numb_2) + " = ").lower()
            if answer_2 == str(rand_numb_1 * rand_numb_2):
                user_input += 1
                print("You got it right!")
                continue

            elif answer_2 == "q":
                break
            
            else:
                print("Better luck next time!")
                continue
    
    elif question_1 == "q":
        break

    else:
        continue

print("You got " + str(user_input) + " questions right!")
print("Thanks for playing!")
sleep(5)
ClearScreen()

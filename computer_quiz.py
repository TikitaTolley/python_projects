# opening:

print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :p")

score = 0

# 1st question:

answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# 2nd question:

answer = input("What does GPU stand for? ")

if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# 3rd question:

answer = input("What does RAM stand for? ")

if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# 4th question: 

answer = input("What does PSC stand for? ")

if answer.lower() == "power supply":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# ending:

print("You got " + str(score) + " questions right!")

print("You got " + str((score/4) * 100) + "%")
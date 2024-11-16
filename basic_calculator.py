# define the functions needed: add, sub, mul, div
# print options to the user
# ask for values
# call the functions
# while loop to continue the program until the user wants to exit

def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer))

def sub(a, b):
    answer = a - b 
    print(str(a) + " - " + str(b) + " = " + str(answer))

def mul(a, b):
    answer = a * b
    print(str(a) + " x " + str(b) + " = " + str(answer))

def div(a, b):
    answer = a / b 
    print(str(a) + " / " + str(b) + " = " + str(answer))
while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    choice = input("Input your choice: ")

    if choice == "A".lower():
        print("Addition!")
        a = int(input("Input your first number: "))
        b = int(input("Input your second number: "))
        add(a, b)

    elif choice == "B".lower():
        print("Subtraction!")
        a = int(input("Input your first number: "))
        b = int(input("Input your second number: "))
        sub(a, b)

    elif choice == "C".lower():
        print("Multiplication!")
        a = int(input("Input your first number: "))
        b = int(input("Input your second number: "))
        mul(a, b)

    elif choice == "D".lower():
        print("Division!!")
        a = int(input("Input your first number: "))
        b = int(input("Input your second number: "))
        div(a, b)

    else:
        print("Program has ended!")
        quit()
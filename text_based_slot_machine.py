# user will deposit a certain amount of money
# they can then bet on either lines: 1, 2 or 3 of the slot machine
# if they got lines, we will multiply their bet by the value of the line
# add this to their balance
# then allow them to keep playing until they want to cash out or run out of money

import random


MAX_LINES = 3   # global constant, doesn't change throughout the program
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {        # the lower the symbol the higher your bet gets multiplied
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):       # if you bet 1 line, it will only check the 1st row (index 0)
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)  # adding 1 so as to not get 0, 1, 2 etc (since its an index)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]    # copies pre. all_symbols
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)

    return columns

def deposit():
    while True:
        amount = input("What would you like to deposit? £")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines

def print_slot_machine(columns):         # transposing a matrix: changing columns that will print in row format to now column format
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):    # enumerate gives index as well as the item
            if i != len(columns) -1:    
                print(column[row], end = " | ")     # by defult, end is equal to the new line character
            else:
                print(column[row], end= "")

        print()     # brings us down to next line



def get_bet():
    while True:
        amount = input("What would you like to bet on each line? £")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between £{MIN_BET}-£{MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is £{balance}")
        else:
            break

    print(f"You are betting £{bet} on {lines} lines. Total bet is equal to: £{total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)     # slots are the columns
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won £{winnings}.")
    print(f"You won on lines:", *winning_lines)    # * is the splat/unpack operator: will pass every line from winning_lines into here, so if we had lines 1 and 2, it'll pass 1 and 2
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is £{balance}")
        answer = input("Press enter to play (q to quit). ")
        if answer == "q":
            break
        balance += spin(balance)
    
    print(f"You left with £{balance}")

main()
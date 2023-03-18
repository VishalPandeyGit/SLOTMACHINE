import random
MAX_LINES = 3
MAX_BET = 10000
MIN_BET = 100
ROWS = 3
COLS = 3

symbol_count = {
    "!": 2,
    "@": 4,
    "#": 6,
    "$": 8
}
symbol_value = {
    "!": 5000,
    "@": 4000,
    "#": 3000,
    "$": 2000
}

def check_winning(columns, lines, bet, values):
    winnings = 0
    winning_lines = [] #to display the winning line
    for line in range(lines): #looping in every row which is every line in the lines
        symbol = columns[0][line]  #check first colum in the current row must be same
        for column in columns:     #loop in every single colum to check symbols
            symbol_to_check = column[line]    #sybmol to check must be equal to colum at the current row
            if symbol != symbol_to_check:   #check if symbols are not same if not same break out
                break
        else:
            winnings += values[symbol] * bet  #if won then the value and sybmbol value multiply by the bet in each line not total bet
            winning_lines.append(lines + 1)   #show the line of winning
    return winnings, winning_lines


def get_slot_machine_spin(ROWS, COLS, symbol_count):  #(4) to run the symbol in game
    all_symbols = [] #list  # taking them in list
    for symbol, symbol_count in symbol_count.items():  #symbol=!@#$ Symbolcount 2468 and symbol item is !1 @2 #3 $4
        for _ in range(symbol_count):  #range 2468
            all_symbols.append(symbol)  #will assign to all symbol list

    columns = []    #defining a colum list
    for _ in range(COLS):  #generating for three col to run 3 times   (-) for not using any values
        column = []  #is equal to empty list
        current_symbols = all_symbols[:]  #to current symbol this line is used : is slice operator [0:2] 0,1,2
        for _ in range(ROWS):  #no of rows
            value = random.choice(current_symbols)  #now any symbol is picked randomly
            current_symbols.remove(value)  #if one symbol is picked in a colum can't repeat
            column.append(value) #add value to colum
        columns.append(column)  #add colum to colums
    return columns

def print_slot_machine(columns):  #to change value from horizotal to vertical (- to |)
    for row in range(len(columns[0])):  #starts from value not empty
        for i, column in enumerate(columns): #change
            if i != len(columns) - 1:    #these if is for A|B|C NOT |A|B|C|
                print(column[row], end=" | ")
            else:
                print(column[row], end="")  #print values in row 0-2
        print()


def deposit():  #function for deposit (1)
    while True: #if function called and true then enter the amount
        amount = input("What would you deposit? Rs.")
        if amount.isdigit(): #check if amount entered is digit +ve
            amount = int(amount) #convert into int
            if amount > 0: #must be more than 0
                break   #come out of statemnt if more than 0 or else
            else:
                print("Amount must be greater than 0.")   #ask for amount again
        else:
            print("Please enter a amount.")   #amount entered is correct
    return amount  #fuction varable


def get_number_of_lines():   #(2)
    while True: #if function called and true then enter the amount
        lines = input("What is the number of lines to bet (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit(): #check if lines entered is digit +ve
            lines = int(lines) #convert into int
            if 1 <= lines <= MAX_LINES: #must be between 1 and max=5
                break   #come out of statemnt if more than 0 or else
            else:
                print("Enter the lines.")   #ask for lines if not in range
        else:
            print("Please enter no of  lines.")   #amount entered is correct
    return lines  #fuction varable

def get_bet():  #(3)
    while True:  # if function called and true then enter the amount
        amount = input("What would you BET? Rs.")
        if amount.isdigit():  # check if amount entered is digit +ve
            amount = int(amount)  # convert into int
            if MIN_BET <= amount <= MAX_BET:  # must be between min and max
                break  # come out of statemnt
            else:
                print(f"Amount must be between Rs.{MIN_BET} - Rs.{MAX_BET}")  # ask for amount
        else:
            print("Please enter a amount.")  # amount entered is correct
    return amount  # fuction varable

def game(balance):
    lines = get_number_of_lines()  # lines to no of lines
    while True:
        bet = get_bet()  # bet to get the amount to be bet
        total_bet = bet * lines
        if total_bet > balance:
            print(f" You have no sufficiant balance to bet,Your balance is Rs.{balance}")
            deposit()
        else:
            break
    print(
        f"You are betting Rs.{bet} on {lines} lines. Total bet is equal to: Rs.{total_bet}")  # printing bet amount multiply by lines

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winnings_lines = check_winning(slots, lines, bet, symbol_value)
    print(f"You WON Rs.{winnings}, and the line is {winnings_lines}.")
    print(f"You WON on lines:", *winnings_lines)
    return winnings - total_bet

def main():   #main function to call and rerun the game
    balance = deposit()  #bal to deposit to get the amount
    while True:
        print(f"Current balance is Rs.{balance}")
        spin = input("Press Enter to SPIN (q to quit).")
        if spin in ["q", "Q"]:  # to quit
            break
        balance += game(balance)
    print(f"You're balance is Rs.{balance}")


main()




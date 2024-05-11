import random # we want the slot machines to generate random values



# global constants to keep the program dynamic and if to be able to change and update the code at one go. And use them anywhere in our project.
MAX_LINES = 3 
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B":4,
    "C":6,
    "D" : 8 
}
symbol_value = {
    "A": 5,
    "B":4,
    "C":3,
    "D" : 2 
}

def check_winnings(columns , lines , bet ,values):
    winnings = 0
    winning_lines = []
    
    for line in range(lines):
        #to check if all the symbols in the line is same
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
# for else loop - if the if condition is true it breaks and not go into the else but if is not true then the else is executed 
           winnings+= values[symbol] * bet
           winning_lines.append(line + 1)
    return winnings , winning_lines



        
# logic to generate items
def get_slot_machine_spin(rows,cols,symbols):
    #random generation of the symbols for each our columns
    all_symbols = []
    for symbol,symbol_count in symbols.items(): # dict.items() gives both the keys and values.
        for _ in range(symbol_count):
            # _ is an anonymous variable in python which means to say that whenever we want to loop through an iterable and we dont care about the iterator value we can use _ and we wont have an unused variable.
            all_symbols.append(symbol)
    columns = []# each of these represent the columns
    # generate columns as many times as the column count. 3 here so the following repeats three times.
    # columns symbolise a list of all the columns [[],[],[]]
    for _ in range(cols):
        column = [] # represents each column one by one for each row
        # created a copy of the symbols' list
        current_symbols = all_symbols[:] 

        for _ in range(rows): # looping through all the values we need to generate for ie rows
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
    return columns
# we need to make a copy so that once is symbol is slected it is removed as we cant have 3 if 1 is removed out of 2 for eg
            
def print_slot_machine(columns):
    #transposing
     for row in range(len(columns[0])):
         
       for i  ,column in enumerate(columns) : 
            # enumerate() returns the index as well as the value of the list 
            # i : index , column : value
            
           # handling the last element.
            if i!=len(columns) - 1:
                print(column[row],end=" | ")
            else:
                print(column[row],end="")
# to move to the next line after printing each row - empty print() statement brings to the new line by default
                
       print()

def deposit():
    # responsible for collecting user input
    while True:
        amount = input("Hello Player! \n Enter your deposit amount : $ ")
        #checking validity of the input
        if amount.isdigit():
             amount = int(amount) # to convert the string (digit input) to int
             if amount > 0 :
                 break
             else :
                 print("! Amount must be greater than $0.")

        else :
            print("Enter a number : ")
    return amount        

def get_number_of_lines():
    while True:
       lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES)+ ") ?")
       if lines.isdigit():
          lines = int(lines)
          if 1<= lines <= MAX_LINES:
              break 
          else :
              print("! Please enter a valid number of lines: ")
    return lines 

def get_bet():
    while True:
        amount = input("What would you like to bet on each line ? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET :
            # valid
               break
            else:
                print(f"! Amount must be between ${MIN_BET}-${MAX_BET}")
                # To automatically convert the variable to a string.

        else :
            print(" ! Please enter a number. ")
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:

       bet = get_bet()
       total_bet = bet * lines
       
       # checking if the player has enough to bet in their balance.
       if total_bet > balance:
         print(f"You don't have enough to bet that amount, your current balance is ${balance}")
       else:
         break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}")
    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings , winning_lines= check_winnings(slots,lines,bet,symbol_value)
    print(f"You won ${winnings}!")
    return winnings - total_bet
    


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit)")
        if answer == "q":
            break
        balance += spin(balance)
    
    print(f"You're left with ${balance}.")

main()
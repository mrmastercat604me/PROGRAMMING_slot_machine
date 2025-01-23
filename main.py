import random, time, sys, os
from other_functions import roll_credits, clear, txt
#IMPORT THESE FUNCTIONS FROM MY FILE

#GLOBAL VARIABLES
MAX_LINES = 3
MIN_LINES = 1
MIN_BET = 1

ROWS = 3
COLS = 3
####


#GLOBAL DICTIONARIES
SYMBOL_COUNT = {
	"A": 6,
	"B": 9,
	"C": 12,
	"D": 12
}

SYMBOL_VALUES = {
	"A": 5,
	"B": 3,
	"C": 2,
	"D": 2
}
####


#GLOBAL LISTS
credits = [
	"PYTHON SLOT MACHINE",
	"CODED BY: duckling604",
	"STRUCTURE BY: @TechWithTim",
	"PROJECT IDEA: David Ashton",
	"ADDITIONAL FEATURES: duckling604"
]
####


#GAME FUNCTIONS
def deposit():
	while True:
		txt("How much would you like to deposit?", end="")
		deposit_amount = input(" $")
		if deposit_amount.isdigit():
			deposit_amount = int(deposit_amount)
			if deposit_amount > 0:
				break
			else:
				txt("Amount must be greater than 0.")
				time.sleep(1)
				clear()
		else:
			txt("Input must be a valid amount.")
			time.sleep(1)
			clear()
	clear()
	return deposit_amount

def bet_number_lines(balance):
	while True:
		txt(f"How many lines would you like to bet on? ({MIN_LINES}-{MAX_LINES})", end="")
		bet_lines = input(": ")
		if bet_lines.isdigit():
			bet_lines = int(bet_lines)
			if bet_lines > balance:
				txt("Number of bet lines must be in range of funds.")
			elif MIN_LINES <= bet_lines <= MAX_LINES:
				break
			else:
				txt(f"Number of bet lines must be in range.")
				time.sleep(1)
				clear()
		else:
			txt("Input must be a valid amount.")
			time.sleep(1)
			clear()
	return bet_lines

def get_bet(balance, lines):
	while True:
		txt(f"How much would you like to bet on each line? (max {balance//lines}) ",end="")
		bet_amount = input(" $")
		if bet_amount.isdigit():
			bet_amount = int(bet_amount)
			if MIN_BET <= bet_amount <= balance//lines:
				break
			else:
				txt(f"Amount must be between. {MIN_BET} and {balance//lines}")
				time.sleep(1)
				clear()
		else:
			txt("Please enter a number.")
			time.sleep(1)
			clear()
	return bet_amount

def gen_slot_machine(rows, cols, symbols):
	all_symbols = []
	for symbol, SYMBOL_COUNT in symbols.items():
		for _ in range(SYMBOL_COUNT):
			all_symbols.append(symbol)
	columns = []
	for _ in range(cols):
		column = []
		current_symbols = all_symbols[:]
		for _ in range(rows):
			value = random.choice(current_symbols)
			current_symbols.remove(value)
			column.append(value)
		columns.append(column)
	return columns

def print_slot_machine(columns):
	print()
	for row in range(len(columns[0])):
		for i, column in enumerate(columns):
			if i != len(columns) -1:
				print(f"{column[row]}", end=" | ")
				# time.sleep(0.7)
			else:
				print(f"{column[row]}")
				# time.sleep(1)
	print()

def slot_spin_visual(slots,rows,cols,symbols,bet,lines,total_bet,times=1):
	slots2 = gen_slot_machine(rows, cols, symbols)
	for itr in range(times):
		#generate slots2 list
		if itr > 0:
			slots2 = gen_slot_machine(rows, cols, symbols)
		for rev_row in range(2,-1,-1):
			for col in range(3):
				sys.stdout.flush()
				time.sleep(0.4)
				clear()
				print(f"You are betting ${bet} on {lines} lines.")
				print(f"Total bet is equal to: ${total_bet}")
				# print(f"print from:  slots[{rev_row}][{col}]  rev_row{rev_row},col{col}")
				# print(f"print to:  slots[0][{col}]  row0,col{col}\n")
				slots2[col].insert(0, slots[col][rev_row])
				del slots2[col][3]
				print_slot_machine(slots2)

def check_winnings(columns, lines, bet, values):
	winnings = 0
	winning_lines = []
	for line in range(lines):
		symbol = columns[line][0]
		for column in columns:
			symbol_to_check = column[line]
			if symbol != symbol_to_check:
				break
		else:
			winnings += values[symbol] * bet
			winning_lines.append(line + 1)
	return winnings, winning_lines
	
def game(balance):
	lines = bet_number_lines(balance)
	while True:
		bet = get_bet(balance, lines)
		total_bet = lines * bet
		if total_bet <= balance:
			break
		else:
			txt(f"Your current balance is: ${balance}. You need to bet a valid amount in range.")
	time.sleep(1)
	clear()
	txt(f"You are betting ${bet} on {lines} lines.")
	txt(f"Total bet is equal to: ${total_bet}")
	time.sleep(0.5)

	slots = gen_slot_machine(ROWS,COLS,SYMBOL_COUNT)
	slot_spin_visual(slots,ROWS,COLS,SYMBOL_COUNT,bet,lines,total_bet)
	time.sleep(1)
	winnings, winning_lines = check_winnings(slots, lines, bet, SYMBOL_VALUES)
	txt(f"You Won ${winnings}")
	if len(winning_lines) > 0:
		if len(winning_lines) == 1:
			txt("You won on line: ", *winning_lines)
		else:
			txt("You won on lines: ", *winning_lines)
	time.sleep(2)
	input("Enter to Continue")
	clear()
	return winnings - total_bet
####

#GAME
if __name__ == '__main__':
	roll_credits(credits,scroll=True)

	# init_balance = deposit()
	# balance = init_balance
	balance = 0
	running = True
	while running:
		txt(f"Current Balance: {balance if balance is not None else 0 }")
		txt("Would you like to (p)lay, (b)alance, or (e)xit?", end="")
		action = input(" : ")
		clear()
		if action.lower() == "e":
			if balance != init_balance:
				txt(f"You left with ${balance}")
			running = False
			break
		elif action.lower() == "b":
			txt("Balance Reset")
			balance = 0
			txt(f"Balance = {balance}")
			time.sleep(1)
			clear()
			init_balance = deposit()
			balance = init_balance
		elif action.lower() == "p":
			balance += game(balance)
		else:
			txt("Please choose an option.")
			time.sleep(0.5)
			clear()
	txt("Thank you for playing")
####
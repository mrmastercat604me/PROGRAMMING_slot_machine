import time
import sys
import os

def txt(*objects,end="\n",speed=0.0695):
	for obj in objects:
		text_str = str(obj)
		for char in text_str:
			print(char, end="")
			sys.stdout.flush()
			time.sleep(speed)
	print("", end=end)

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')


def roll_credits(credits, screen_length=4, line_time=2,scroll=True):
	line_count = 0
	if screen_length > len(credits):
		screen_length = len(credits)
	clear()
	if scroll:
		for line, _ in enumerate(credits):
			while line_count < screen_length:
				for count in range(line, line + screen_length):
					print(credits[count])
					sys.stdout.flush()
					time.sleep(line_time)
					line_count += 1
				clear()
			else:
				line += 1
				if line < len(credits):
					if len(credits) - line >= screen_length:
						for count in range(line, line + screen_length):
							print(credits[count])
							sys.stdout.flush()
					else:
						for count in range(line, len(credits)):
							print(credits[count])
							sys.stdout.flush()
				time.sleep(line_time)
				clear()
	else:
		for line, _ in enumerate(credits):
			print(credits[line])
			sys.stdout.flush()
			time.sleep(line_time)
		clear()
		
####

if __name__ == '__main__':
	txt("cheese?")
	#TESTING TXT FUNCTION
	time.sleep(2)
	#ESTABLISHING TEST CREDITS LIST
	credits = [
		"Line 1 Credit",
		"Line 2 Credit",
		"Line 3 Credit",
		"Line 4 Credit",
		"Line 5 Credit",
		"Line 6 Credit",
		"Line 7 Credit",
		"Line 8 Credit",
		"Line 9 Credit",
		"Line 10 Credit"
	] 
	roll_credits(credits)
	#TESTING ROLL_CREDITS FUNCTION
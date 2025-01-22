from other_functions import clear


def deep_copy(lst):
	return [deep_copy(item) if isinstance(item, list) else item for item in lst]


col1 = ['A','B','C']
col2 = ['A','B','C']
col3 = ['A','B','C']

og_slots = [col1,col2,col3]
slots = deep_copy(og_slots)

col2_1 = ['D','E','F']
col2_2 = ['D','E','F']
col2_3 = ['D','E','F']

slots2 = [col2_1,col2_2,col2_3]

def print_slots(columns):
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

print_slots(slots)
print()
print_slots(slots2)
print("------------------\n")
print_slots(slots)
print("-----")


#slots[column][row]
def slot_spin_visual(slots,slots2):
	times = int(input("How many times?: "))
	for time in range(times):
		#generate slots2 list
		if time > 0:
			global og_slots
			slots2 = deep_copy(og_slots)
		for rev_row in range(2,-1,-1):
			for col in range(3):
				input("Enter")
				clear()
				print(f"print from:  slots[{rev_row}][{col}]  rev_row{rev_row},col{col}")
				print(f"print to:  slots[0][{col}]  row0,col{col}\n")
				slots2[col].insert(0, slots[col][rev_row])
				del slots2[col][3]
				print_slots(slots2)


slot_spin_visual(slots, slots2)



#WORKING ROW SLIDE
# for rev_slot_index in range(len(slots2)-1, -1, -1):
#     slots.insert(0, slots2[rev_slot_index])
#     del slots[3]
#     for i, row in enumerate(slots):
#         print(*row)
#     print("--------------")

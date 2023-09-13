import random
import os
import time

computer_board = [] #two-dimensional list with a list of target cells hidden from the user
user_board = [] #two-dimensional list(game board) displayed on the user's screen
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'] #list of letters used to assign the columns of the game board
count_hit = 0 #variable used to count the found target cells by the user
count_missed = 0 #variable used to count missed shots
second_column = -1 #variable used to find the other end(column) of the ship
second_row = -1  #variable used to find the other end (column) of the ship
user_cell_repeated = '' #variable used to check whether coordinate was entered earlier or not
checked = 0 #variable used to check the validity of the entered dimension

os.system("clear")
print("BATTLESHIP GAME")
print("The ship is randomly placed by the computer on the board within 4 consecutive cells")
DIMENSION = input("Enter the board dimension(if 4x4, enter only 4): ")

def board():
	num = 1
	os.system("clear")
	print("BATTLESHIP GAME")
	print("\n", end=" ")
	for n in range(DIMENSION):
		print(' ',letters[n], end = ' ')
	print('')
	for c in range(DIMENSION):
		if num == 10:
			print(num,"", end='')
		else:
			print(num,' ', end='')
		num = num + 1
		for d in range(DIMENSION):
			print(user_board[c][d], end=' | ')
		print('')
		for f in range(DIMENSION*2):
			print('--', end='')
		print('--', end='')
		print()	
	num = 1
	print('\n'"Attempts(missed): ", count_missed)
	print("Found cells: ", count_hit)


''' 
lines of code used to verify the validity of the dimension size entered by the user
'''
while checked == 0:
	while DIMENSION.isdigit() == False or int(DIMENSION) > 10 or int(DIMENSION) < 4:
		os.system("clear")
		print("BATTLESHIP GAME")
		print("The ship is randomly placed by the computer on the board within 4 consecutive cells")
		DIMENSION = input("Please enter valid dimension(if 4x4, enter only 4): ")
		if DIMENSION.isdigit() == True and 4 <= int(DIMENSION) <= 10:
			checked = 1
	checked = 1


DIMENSION = int(DIMENSION)

''' 
lines of code used to create 2d boards
'''
for a in range(DIMENSION):
	user_row = []
	for b in range(DIMENSION):
		user_row.append(' ')
	user_board.append(user_row)

for a in range(DIMENSION):
	computer_row = []
	for b in range(DIMENSION):
		computer_row.append('#')
	computer_board.append(computer_row)


''' 
lines of code used to assign a random coordinate to the ship (coordinates: [first_row][first_column])
'''
first_column = random.randint(0, DIMENSION-1)
first_row = random.randint(0, DIMENSION-1)
computer_board[first_row][first_column] = 'X'


''' 
lines of code used to determine whether the ship will be placed vertically or horizontally
'''
choosing_orientation = random.randint(0, 1) 
if choosing_orientation == 0: #choosing_orientation = 0 -> horizontally
	if DIMENSION < 6:
		if DIMENSION == 4:
			for r in range(0, DIMENSION):
				computer_board[r][first_column] = 'X'
		else:
			choosing_empty_cell = random.randint(0, 1)
			if choosing_empty_cell == 0:
				for h in range(0, DIMENSION-1):
					computer_board[h][first_column] = 'X'
			else:
				for j in range(1, DIMENSION):
					computer_board[j][first_column] = 'X'
	else:	
		while second_column > (DIMENSION - 1) or second_column < 0:
			first_column_extend = random.randint(0, 1)
			if first_column_extend == 0:
				second_column = first_column - 3 #placing the other end on the left side
			else:
				second_column = first_column + 3 #placing the other end on the right side
		computer_board[first_row][second_column] = 'X' #labeling 'X' other end of the ship(X # # X)
		if second_column > first_column: #checking where second cell is placed(left or right) 
			computer_board[first_row][first_column + 1] = 'X' #labeling cells between 2 ends
			computer_board[first_row][first_column + 2] = 'X' #labeling cells between 2 ends
		else:
			computer_board[first_row][first_column - 1] = 'X' #labeling cells between 2 ends
			computer_board[first_row][first_column - 2] = 'X' #labeling cells between 2 ends
else: #choosing_orientation = 1 -> vertically
	if DIMENSION < 6:
		if DIMENSION == 4:
			for r in range(0, DIMENSION):
				computer_board[first_row][r] = 'X'
		else:
			choosing_empty_cell = random.randint(0, 1)
			if choosing_empty_cell == 0:
				for h in range(0, DIMENSION-1):
					computer_board[first_row][h] = 'X'
			else:
				for j in range(1, DIMENSION):
					computer_board[first_row][j] = 'X'
	else:
		while second_row > (DIMENSION - 1) or second_row < 0:
			first_row_extend = random.randint(0, 1)
			if first_row_extend == 0:
				second_row = first_row - 3 #placing the other end down
			else:
				second_row = first_row + 3 #placing the other end up
		
		computer_board[second_row][first_column] = 'X' #labeling 'X' the other end of the ship(X # # X)
		if second_row > first_row: #checking where second cell is placed(up or down) 
			computer_board[first_row + 1][first_column] = 'X' #labeling cells between 2 ends
			computer_board[first_row + 2][first_column] = 'X' #labeling cells between 2 ends
		else:
			computer_board[first_row - 1][first_column] = 'X' #labeling cells between 2 ends
			computer_board[first_row - 2][first_column] = 'X' #labeling cells between 2 ends
	
valid_test_column = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'] #list used to check the validity of the coordinate and convert the entered cell coordinate into indexed lists(column index)
valid_test_row = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'] #list used to check the validity of the coordinate and convert the entered cell coordinate into indexed lists(row index)

''' 
lines of code used to remove unnecessary items from the list
'''
for o in range(DIMENSION+1, 10):
	h = DIMENSION
	valid_test_column.pop(h)
	valid_test_row.pop(h)

#game area:
while count_hit != 4: #if count = 4 game is won
	board() #board display

	'''
	checking whether cell is entered repeteadly or not
	'''
	if user_cell_repeated != '':
		print('Please, enter new coordinates, ', user_cell_repeated, ' was previously entered: ')
		time.sleep(0.5)


	user_cell = input('\n'"Enter the coordinate: ")
	user_cell_list = list(user_cell) #creating list - 'A5' -> ['A', '5']

	while len(user_cell_list) != 2 and len(user_cell_list) != 3:
		user_cell = input("Please enter valid coordinates: ")
		user_cell_list = list(user_cell) #creating list - 'A5' -> ['A', '5']

	user_cell_list = list(user_cell) #creating list - 'A5' -> ['A', '5']
	
	''' 
	lines of code used to check the validity of the coordinates entered by the user
	'''
	if DIMENSION != 10:
		while len(user_cell_list) != 2:
			user_cell = input("Please enter valid coordinates: ")
			user_cell_list = list(user_cell) #creating list - 'A5' -> ['A', '5']

	if len(user_cell_list) == 3:
			user_cell_list[1] = user_cell_list[1] + user_cell_list[2] #when user enter A10, in the list it will appear like - ['A', '10']
			user_cell_list.pop() #deleting 3rd item in the list

	while valid_test_column.count(user_cell_list[0]) != 1 or valid_test_row.count(user_cell_list[1]) != 1:
		user_cell = input("Please enter valid coordinates: ")
		user_cell_list = list(user_cell) #creating list - 'A5' -> ['A', '5']
		while len(user_cell_list) != 2 and len(user_cell_list) != 3:
			user_cell = input("Please enter valid coordinates: ")
			user_cell_list = list(user_cell) #creating list - 'A5' -> ['A', '5']
		if len(user_cell_list) == 3:
			user_cell_list[1] = user_cell_list[1] + user_cell_list[2] #when user enter A10, in the list it will appear like - ['A', '10']
			user_cell_list.pop() #deleting 3rd item in the list

	'''
	lines of code used to convert user coordinates into computer coordinates that are understandable to the list 
	'''
	computer_cell_column = valid_test_column.index(user_cell_list[0]) #translating entered column into list index
	computer_cell_row = valid_test_row.index(user_cell_list[1]) #translating entered row into list index


	if user_board[computer_cell_row][computer_cell_column] == '#' or user_board[computer_cell_row][computer_cell_column] == 'X': #checking whether the coordinates were entered repeatedly or not
		user_cell_repeated = user_cell
	else:
		''' 
		lines of code used to check whether the user has found the target cell or not
		'''
		if computer_board[computer_cell_row][computer_cell_column] == '#': #user missed the target, wrong coordinate
			print('Missed! Try harder...')
			time.sleep(0.8)
			user_board[computer_cell_row][computer_cell_column] = '#' #labeling missed cell on the board
			count_missed = count_missed + 1 #counting missed cells(attempts)
			user_cell = ''
			user_cell_list = ''
			user_cell_repeated = ''
		else: #user hit the target
			print('GOOD SHOT!')
			time.sleep(0.8)
			user_board[computer_cell_row][computer_cell_column] = 'X' #labeling targeted cell on the board
			count_hit = count_hit + 1 #counting found target cells
			user_cell = ''
			user_cell_list = ''
			user_cell_repeated = ''

#game is won:
board() #board display
print("GAME")
time.sleep(0.35)
print("IS")
time.sleep(0.35)
print("OVER")
time.sleep(0.35)
print("!!!")
time.sleep(0.35)
print('\n''THE MISSION IS COMPLETED!!! The Enemy Ship is DESTROYED!!!')
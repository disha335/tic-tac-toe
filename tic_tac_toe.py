board = [' ' for x in range(1,10)]

def InsertLetter(letter,pos):
	board[pos] = letter

def IsSpaceFree(pos):
	return board[pos] == ' '

#printing the game board
def printBoard(board):
	print('   |   |   ')
	print(' ' + board[1] +' | '+board[2] + ' | '+board[3])
	print('   |   |   ')
	print('------------')

	print('   |   |   ')
	print(' ' + board[4] +' | '+board[5] + ' | '+board[6])
	print('   |   |   ')
	print('------------')

	print('   |   |   ')
	print(' ' + board[7] +' | '+board[8] + ' | '+board[9])
	print('   |   |   ')
	
#check if the board is full
def isBoardFull(board):
	if board.count(' ') > 1:
		return False
	else:
		return True

def isWinner(b,l):
	return ((b[1]== l and b[2]== l and b[3]== l) or 
	(b[4] == l and b[5] == l and b[6] == l)or
	(b[7] == l and b[8] == l and b[9] == l)or
	(b[1] == l and b[4] == l and b[7] == l)or
	(b[2] == l and b[5] == l and b[8] == l)or
	(b[3] == l and b[6] == l and b[9] == l)or
	(b[1] == l and b[5] == l and b[9] == l)or
	(b[3] == l and b[5] == l and b[7] == l))  #here's the winner.

#user move is defined in this function

def playerMove():
	run = True
	while run == True:
		move = input("Please select a position to enter the X between 1 and 9..")
		try:
			move = int(move)
			if move > 0 and move < 10:
				if IsSpaceFree(move):
					run = False
					InsertLetter('X',move)
				else:
					print("Sorry this space is occupied.")
			else:
				print("You can only write numbers that are between 1 and 9.")

		except:
			print("Please type a number.")

#computer move
def computerMove():
	possibleMoves = [x for x ,letter in enumerate(board) if letter == ' ' and x != 0]
	move = 0
	for j in ['O','X']:
		for i in possibleMoves:
			boardCopy = board[:] 
			boardCopy[i] = j
			if isWinner(boardCopy,j):
				move = i
				return move

	cornerOpen = []
	for i in possibleMoves:
		if i in [1,3,7,9]:
			cornerOpen.append(i)
	if len(cornerOpen) > 0:
		move = selectRandom(cornerOpen)
		return move

	if 5 in possibleMoves:
		move = 5
		return move

	edgesOpen = []
	for i in possibleMoves:
		if i in [2,4,6,8]:
			edgesOpen.append(i)

	if len(edgesOpen) > 0:
		move = selectRandom(edgesOpen)
		return move

def selectRandom(li):
		import random
		lt = len(li)
		r = random.randrange(0,lt)
		return li[r]

def main():
		print("Welcome to the game!")
		printBoard(board)

		while not(isBoardFull(board)):
			if not(isWinner(board,'O')):
				playerMove()
				printBoard(board)
			else:
				print("Oops!!You lose")
				break

			if not(isWinner(board, 'X')):
				move = computerMove()
				if move == 0:
					print(" ")
				else:
					InsertLetter('O' , move)
					print("Computer placed O on position" , move , ':')
					printBoard(board)
			else:
				print("Congratulations!!You win.")
				break

		if isBoardFull(board):
			print("It's a tie.")


while True:
    x = input("Do you want to play ? (y/n)")
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print('--------------------')
        main()
    elif x.lower() == 'n':
        break
    else:
    	print("Type either y or n")

#code by Disha Handa


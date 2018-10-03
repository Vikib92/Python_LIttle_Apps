#! /usr/bin/Python

import random

def print_brd(brd):
	print('\n'*15)
	print('-------------')
	print('| '+ brd[1] + ' | ' + brd[2] + ' | ' + brd[3] + ' |')
	print('-------------')
	print('| '+ brd[4] + ' | ' + brd[5] + ' | ' + brd[6] + ' |')
	print('-------------')
	print('| '+ brd[7] + ' | ' + brd[8] + ' | ' + brd[9] + ' |')
	print('-------------')

def player_inp():
	markr = ' '
	while not (markr == 'X' or markr == 'O'):
		markr = input("Do you want to be X or O, Player 1 ? ").upper()
	
	if markr == 'X':
		return ('X','O')
	else:
		return ('O','X')

def win_check(brd,markr):
	return ((brd[1] == brd[2] == brd[3] == markr) or 
		(brd[1] == brd[4] == brd[7] == markr) or 
		(brd[1] == brd[5] == brd[9] == markr) or 
		(brd[3] == brd[6] == brd[9] == markr) or
		(brd[3] == brd[5] == brd[7] == markr) or 
		(brd[4] == brd[5] == brd[6] == markr) or
		(brd[7] == brd[8] == brd[9] == markr))	 
	
def full_check(brd):
	return " " not in brd[1:]

def get_pos(brd,markr):
	while True:
		try:
			pos = int(input("Enter the position from 1 - 9 : "))
		except ValueError:
			print("Enter a valid input")
			continue

		if (pos not in range(1,10)) or ( " " not in brd[pos]):
			print("You entered an incorrect value or there is already a value in that position")
			continue
		
		brd[pos] = markr
		break

def playr_sw(brd,markr,game_on):

	print_brd(brd)
	print("Select position for value " + markr)
	get_pos(brd,markr)
	announce = ' '

	if full_check(brd):
		announce = "tie"
		game_on = False

	if win_check(brd,markr):
		announce = "won"
		game_on = False

	return game_on,announce

def main():
	print("Welcome to Tic Tac Toe!!!")

	brd = [' '] * 10
	pl1, pl2 = player_inp()
	game_on = True
	
	while True:

		game_on,announce = playr_sw(brd,pl1,game_on)

		if announce == "won":
			print_brd(brd)
			print("Congrats Player 1!!! You have won the game")
		elif announce == "tie":
			print_brd(brd)
			print("The game is tied")
		
		if game_on == False:
			break
	
		game_on,announce = playr_sw(brd,pl2,game_on)

		if announce == "won":
			print_brd(brd)
			print("Congrats Player 2!!! You have won the game")
		elif announce == "tie":
			print_brd(brd)
			print("The game is drawn")
		
		print_brd(brd)
		if game_on == False:
			break
		
	choice = input('Do you want to play again? Enter Yes or No: ').lower()
	if choice == 'yes':
		main()
	else:
		print("Thanks for playing !!!")

if __name__ == "__main__":main()

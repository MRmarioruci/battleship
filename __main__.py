from termcolor import colored
from classes.Game import Game

print('Welcome to BATTLESHIP MOTHERFUCKER')
start = input("Ready to start the game? (Yes = y, No = n): ")

if start == 'y':
	game = Game()
	game.init()
	'''while game.winner == None:
		#as'''
else:
	print('Game aborted')
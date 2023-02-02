from termcolor import colored
from .Board import Board

class Player:
	def __init__(self, rows, columns) -> None:
		self.rows = rows
		self.columns = columns
		self.name = None
		self.board = None
		self.checking = 'c'
		self.manualShipPlacement = False
  	
	def init(self, i):
		name = input(f"Player {i} enter your name: ")
		self.name = name			
		self.checking = input(f"Will your steps be checked by a human(h) or a computer(c)?: ")
		
		if self.checking == 'h':
			self.manualShipPlacement = True if input(f"Do you want to place your ships manually?(y)(n): ") == 'y' else False
		
		print(colored('---------- SUMMARY -------------', 'red'))
		print(f"Name: {colored(self.name, 'green')}")
		print(f"Checking: {colored('human' if self.checking == 'h' else 'computer', 'green')}")
		print(f"Ship placement: {colored('Manual' if self.manualShipPlacement else 'Auto', 'green')} \n")
		self.board = Board(self.rows, self.columns)
		self.board.print()
  
	def getManualPlacement(self):
		return self.manualShipPlacement

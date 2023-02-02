import uuid
import random
from .Player import Player
from .Ships import AircraftCarrier, Destroyer, Submarine

class Game:
	def __init__(self) -> None:
		self.winner = None
		self.c = []
		self.rounds = None
		self.rows = 0
		self.columns = 0
		self.players = []
		self.availableShips = [
			AircraftCarrier(),
   			AircraftCarrier(),
   			Destroyer(),
      		Destroyer(),
      		Destroyer(),
      		Submarine(),
        	Submarine()
		]
	
	def init(self):		
		while self.rows < 5:
			self.rows = int(input(f"Please enter the number of rows you want your board to have.(min 5): "))
		while self.columns < 5:
			self.columns = int(input(f"Now enter the number of columns you want your board to have.(min 5): "))

		self.players = [Player(self.rows, self.columns), Player(self.rows, self.columns)]
		for idx, player in enumerate(self.players):
			player.init(idx+1)
		
		gameEnding = input("\nThe game ends (a) When all the ships of a player are sinked, (b) In a given amount of rounds: ")
		if gameEnding == 'b':
			self.gameRounds = int(input("How many rounds do you want?: "))
   
		print("\nGenerating board...\n")
		self.placeShips()
  
	def placeShips(self):
		maxTries = self.rows * self.columns
		for player in self.players:
			if player.manualShipPlacement:
				print('Manual placement')
			else:
				for ship in self.availableShips:
					placed = False
					remainingTries = maxTries
					isHorizontal = random.getrandbits(1)
					while not placed and remainingTries > 0:
						if isHorizontal:
							maxX = self.rows - ship.positions
							maxY = self.columns
							if maxX < 0:
								isHorizontal = not isHorizontal							
						else:
							maxX = 0
							maxY = self.columns - ship.positions
							if maxY < 0:
								isHorizontal = not isHorizontal
						x = random.randint(0, maxX)
						y = random.randint(0, maxY)

						if self.canPlaceShip(x, y, ship.positions):
							break							
   	
						remainingTries -= 1
       
					
	def canPlaceShip(self, x, y, positions):
		print(f"{x}{y}{positions}")
class Cell:
    def __init__(cell) -> None:
        cell.checked = False
        cell.character = '.'
        cell.points = 0
  
class Board:
	def __init__(self, rows, columns) -> None:
		self.ships = []
		self.board = [[ Cell() for _ in range(columns)] for _ in range(rows)]

	def print(self):
		r = "   "
		for i in range(len(self.board[0])):
			r = f"{r} {i+1}"
		print(r)
		for idx, row in enumerate(self.board):
			r = f"{(idx+1)} |"
			for j in row:
				r  = f"{r} {j.character}"
			print(r)
				
       

class Ship:
    def __init__(ship) -> None:
        ship.bow = None
        ship.direction = None
    
class AircraftCarrier(Ship):
    def __init__(carrier) -> None:
        super().__init__()
        carrier.positions = 5
        carrier.points = 5
        carrier.char = 'A'

class Destroyer(Ship):
    def __init__(destroyer) -> None:
        super().__init__()
        destroyer.positions = 3
        destroyer.points = 2
        destroyer.char = 'D'
        
class Submarine(Ship):
    def __init__(sub) -> None:
        super().__init__()
        sub.positions = 1
        sub.points = 3
        sub.char = 'S'
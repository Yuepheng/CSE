class Room(object):
    def __init__(self, description, name=None, north=None, south=None, east=None, west=None, southeast=None,
                 northeast=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.southeast = southeast
        self.northeast = northeast
        self.description = description


# Option 1 - Use the Variables, but fix later
R19A = Room("Mr. Wade's Room",)
parking_lot = Room("The Parking Lot", None, R19A)
Amphitheater = Room("The stage Outside", None, R19A)
Cafeteria = Room("The Place to get food and chill", None, Amphitheater,)
SB20 = Room("Mr Yang's Room", None, Cafeteria, parking_lot)
Downtown_Dresno = Room("The City of Dresno", None, parking_lot)
Ethan_James_High_School = Room("Ethan James High School Grades 9-12", None, Downtown_Dresno)
Grandparents_House = Room("The house that my grandparents live in.", None, Ethan_James_High_School, Downtown_Dresno)
Parents_House = Room("My mom, dad, 2 sisters and 1 brother live here", None, Grandparents_House)
Office = Room("The Front desk of Ethan James High school", None, R19A)
San_Framsico = Room("The City of Rich People AKA San Framsico", None, Downtown_Dresno)
Cousins_House = Room("My Cousins live here", None, Parents_House)
R13B = Room("Mr. Dawson's Room", None, SB20, R19A)
SL15 = Room("Mrs. Hazen's Biology Room", None, R13B, SB20, R19A,)
J_Mart = Room("The J mart to get food, technology, clothing etc.", None, Downtown_Dresno, Parents_House)


Parents_House.south = J_Mart
Downtown_Dresno.north = J_Mart
R19A.east = SL15
SB20.south = SL15
R13B.north = SL15
R19A.south = R13B
SB20.north = R13B
Parents_House.north = Cousins_House
Downtown_Dresno.north = San_Framsico
R19A.north = Office
Grandparents_House.north = Parents_House
Downtown_Dresno.south = Grandparents_House
Ethan_James_High_School.north = Grandparents_House
Downtown_Dresno.north = Ethan_James_High_School
parking_lot.north = Downtown_Dresno
parking_lot.south = SB20
Cafeteria.north = SB20
Amphitheater.north = Cafeteria
R19A.west = Amphitheater
R19A.north = parking_lot  # Creates a Key when You type north

# Option 2 - Use strings, but more difficult controller
R19A = Room("Mr. Wade's Room")
parking_lot = Room("The Parking Lot", None, R19A)

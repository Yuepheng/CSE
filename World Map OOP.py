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
Downtown_Dresno = Room("The City of Dresno", None,)
Ethan_James_High_School = Room("Ehthan James High School Grades 9-12", None)


Amphitheater.north = Cafeteria
R19A.west = Amphitheater
R19A.north = parking_lot  # Creates a Key when You type north

# Option 2 - Use strings, but more difficult controller
R19A = Room("Mr. Wade's Room")
parking_lot = Room("The Parking Lot", None, R19A)

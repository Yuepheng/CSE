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
R19A = Room("Mr. Wade's Room")
parking_lot = Room("The Parking Lot", None, R19A)

R19A.north = parking_lot

# Option 2 - Use strings, but more difficult controller
R19A = Room("Mr. Wade's Room")
parking_lot = Room("The Parking Lot", None, R19A)

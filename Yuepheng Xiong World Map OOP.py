class Item(object):
    def __init__(self, name):
        self.name = name


class ModeOfTransportation(Item):
    def __init__(self, name):
        super(ModeOfTransportation, self).__init__(name)


class Sedan(ModeOfTransportation):
    def __init__(self, name):
        super(Sedan, self).__init__(name)
        self.Oil_Level = 100
        self.battery_voltage = 15.7
        self.fuel_level = 100
        self.engine_on = False

    def amount_of_oil(self):
        self.Oil_Level -= .001
        print("The Oil gauge reads that I still have LOTS of oil")

    def the_battery_supplying_to_starter(self):
        self.battery_voltage -= .005
        print("The voltage meter reads that it is between 12 and 16 volts")

    def amount_of_fuel(self):
        self.fuel_level -= .0001
        print("The Fuel gauge needle is on F for Full")

    def starting_the_engine(self):
        self.engine_on = True
        print("I started the engine by stepping on the clutch and turning the key")

    def move(self):
        self.Oil_Level -= .001
        self.fuel_level -= .0001
        print("Good thing this Sedan has Power steering")


class HondaAccord(Sedan):
    def __init__(self):
        super(HondaAccord, self).__init__("HondaAccord")


class ToyotaCamry(Sedan):
    def __init__(self):
        super(ToyotaCamry, self).__init__("ToyotaCamry")

    def starting_the_engine(self):
        self.engine_on = False
        print("I started the engine by Turning the key")


class NissanGTR(Sedan):
    def __init__(self):
        super(NissanGTR, self).__init__("NissianGTR")

    def starting_the_engine(self):
        self.engine_on = False
        print("I started the GTR by stepping on the brake and pushing the start button")


class Case(Item):
    def __init__(self, name):
        super(Case, self).__init__(name)


class HdCase(Case):
    def __init__(self, name):
        super(HdCase, self).__init__(name)
        self.size = 48
        self.ram_slots = 4
        self.power_supply = None
        self.hard_drive = None
        self.motherboard = True


class HdPavilionDesktop(HdCase):
    def __init__(self):
        super(HdPavilionDesktop, self).__init__("HdPavalionDesktop")


class ComputerParts(Item):
    def __init__(self, name):
        super(ComputerParts, self).__init__(name)


class AcPowerSupply(ComputerParts):
    def __init__(self, name):
        super(AcPowerSupply, self).__init__(name)
        self.Watts = 500


class Cpu(ComputerParts):
    def __init__(self, name):
        super(Cpu, self).__init__(name)
        self.Gigahertz = 3.20
        self.Cores = 4
        self.virtual_cores = 4


class Cpu2(ComputerParts):
    def __init__(self, name):
        super(Cpu2, self).__init__(name)
        self.Gigahertz = 4.50
        self.Cores = 8
        self.virtual_cores = 12


class Cpu3(ComputerParts):
    def __init__(self, name):
        super(Cpu3, self).__init__(name)
        self.Gigahertz = 2.40
        self.Cores = 2
        self.virtual_cores = 2


class Cpu4(ComputerParts):
    def __init__(self, name):
        super(Cpu4, self).__init__(name)
        self.Gigahertz = 7.70
        self.Cores = 16
        self.virtual_cores = 16


class MotherBoard(ComputerParts):
    def __init__(self, name):
        super(MotherBoard, self).__init__(name)
        self.cpu_slot = True
        self.ram_slots = 4
        self.Pcix16 = True
        self.power_supply_connector = True
        self.hard_drive_connector_wires = True
        self.sata = True
        self.cmos = True


class MotherBoard3(ComputerParts):
    def __init__(self, name):
        super(MotherBoard3, self).__init__(name)
        self.cpu_slot = True
        self.ram_slots = 6
        self.Pcix16 = True
        self.power_supply_connector = True
        self.hard_drive_connector_wires = False
        self.sata = True
        self.cmos = True


class MotherBoard2(ComputerParts):
    def __init__(self, name):
        super(MotherBoard2, self).__init__(name)
        self.cpu_slot = True
        self.ram_slots = 2
        self.Pcix16 = False
        self.power_supply_connector = False
        self.hard_drive_connector_wires = True
        self.sata = True
        self.cmos = False


class MotherBoard4(ComputerParts):
    def __init__(self, name):
        super(MotherBoard4, self).__init__(name)
        self.cpu_slot = True
        self.ram_slots = 4
        self.Pcix16 = True
        self.power_supply_connector = False
        self.hard_drive_connector_wires = True
        self.sata = True
        self.cmos = False


class Memory(ComputerParts):
    def __init__(self, name, ddr3):
        super(Memory, self).__init__(name)
        self.type = ddr3
        self.amount = 12
        self.speed = 1600


class MemoryFaster(ComputerParts):
    def __init__(self, name, ddr4):
        super(MemoryFaster, self).__init__(name)
        self.type = ddr4
        self.amount = 32
        self.speed = 2666


class HardDrive2(ComputerParts):
    def __init__(self, name, windows10pro,):
        super(HardDrive2, self).__init__(name)
        self.storage = 1000
        self.type = hdd
        self.speed = 100
        self.os = windows10pro


class HardDrive3(ComputerParts):
    def __init__(self, name, ssd, windows10home):
        super(HardDrive3, self).__init__(name)
        self.storage = 4000
        self.type = ssd
        self.speed = 500
        self.os = windows10home


class HardDrive4(ComputerParts):
    def __init__(self, name, ssd, windows10home):
        super(HardDrive4, self).__init__(name)
        self.storage = 8000
        self.type = ssd
        self.speed = 1000
        self.os = windows10home


class HardDrive(ComputerParts):
    def __init__(self, name, ssd, windows10home):
        super(HardDrive, self).__init__(name)
        self.storage = 500
        self.type = ssd
        self.speed = 300
        self.os = windows10home


class PowerSupply(ComputerParts):
    def __init__(self, name, ac, generic):
        super(PowerSupply, self).__init__(name)
        self.power = 500
        self.type = ac
        self.size = generic


class PowerSupply2(ComputerParts):
    def __init__(self, name, ac, aftermarket):
        super(PowerSupply2, self).__init__(name)
        self.power = 770
        self.type = ac
        self.size = aftermarket


class PhoneBrand(Item):
    def __init__(self, name):
        super(PhoneBrand, self).__init__(name)


class Applie(PhoneBrand):
    def __init__(self, name):
        super(Applie, self).__init__(name)


class SamSong(PhoneBrand):
    def __init__(self, name):
        super(SamSong, self).__init__(name)


class GalaxyS4(SamSong):
    def __init__(self, name, excellent):
        super(GalaxyS4, self).__init__(name)
        self.storage = 16
        self.os = 4.4
        self.camera = 13
        self.condition = excellent


class GalaxyS3(SamSong):
    def __init__(self, name, excellent):
        super(GalaxyS3, self).__init__(name)
        self.storage = 32
        self.os = 4.2
        self.camera = 8
        self.condition = excellent


class GalaxyS7(SamSong):
    def __init__(self, name, excellent):
        super(GalaxyS7, self).__init__(name)
        self.storage = 64
        self.os = 7
        self.camera = 14
        self.condition = excellent


class APhone8(Applie):
    def __init__(self, name, mint):
        super(APhone8, self).__init__(name)
        self.storage = 64
        self.os = 12
        self.camera = 13
        self.condition = mint


class APhone10F(Applie):
    def __init__(self, name, good):
        super(APhone10F, self).__init__(name)
        self.storage = 128
        self.os = 12
        self.camera = 15
        self.condition = good


class Room(object):
    def __init__(self, description, name=None, north=None, south=None, east=None, west=None, southeast=None,
                 northeast=None, items=None):

        if items is None:
            items = []
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.southeast = southeast
        self.northeast = northeast
        self.description = description
        self.items = items


class Player(object):
    def __init__(self, starting_location):
        self.health = 100
        self.inventory = []
        self.current_location = starting_location

    def move(self, new_location):           # Changes what Room You're in
        """This method moves a player to a new location

        :param new_location: The room object that we move to
        """
        self.current_location = new_location

    def find_room(self, direction):             # Turn a Direction into a Room Object
        """This method takes a direction, and finds the variable of the Room

        :param direction:A string (all lowercase), with a cardinal direction
        :return: A Room object if it exists, None if it does not
        """
        return getattr(self.current_location, direction)
        # getattr(R19A, "north")


CentralProcessingUnit4 = Cpu4(None)
CentralProcessingUnit3 = Cpu3(None)
CentralProcessingUnit2 = Cpu2(None)
CentralProcessingUnit = Cpu(None)
Computer4 = MotherBoard4(None)
Computer3 = MotherBoard3(None)
Computer2 = MotherBoard2(None)
Computer1 = MotherBoard(None)
Ram2 = MemoryFaster(None, ddr4=True)
Ram1 = Memory(None, ddr3=True)
SamSong3 = GalaxyS3(None, excellent=True)
SamSong2 = GalaxyS4(None, excellent=True)
SamSong1 = GalaxyS7(None, excellent=True)
Applie = APhone8(None, mint=True)
Toyota = ToyotaCamry()
Nissan = NissanGTR()
Honda = HondaAccord()
hdd = HardDrive(None, ssd=True, windows10home=True,)
hd2 = HardDrive2(None, windows10pro=True,)
hd3 = HardDrive3(None, ssd=True, windows10home=True,)
hd = HardDrive4(None, ssd=True, windows10home=True)


# Option 1 - Use the Variables, but fix later
R19A = Room("Mr. Wade's Room", "This is the room you are in")
parking_lot = Room("The Parking Lot", "THere are a few cars parked here", None, R19A)
Amphitheater = Room("The stage Outside", "There might be some items here", None, R19A)
Cafeteria = Room("The Place to get food and chill", "There is some leftover non eaten baked ham and cheese bars and"
                                                    "there might be some items here", None, Amphitheater,)
SB20 = Room("Mr Yang's Room", "This guy loves Anime", None, Cafeteria, parking_lot)
Downtown_Dresno = Room("The City of Dresno", "There are a lot of work offices here", None, parking_lot)
Ethan_James_High_School = Room("Ethan James High School Grades 9-12", "The School", None, Downtown_Dresno)
Grandparents_House = Room("The house that my grandparents live in.", "There could be some items here", None,
                          Ethan_James_High_School, Downtown_Dresno)
Parents_House = Room("My mom, dad, 2 sisters and 1 brother live here", "There could be some helpful items here", None,
                     Grandparents_House)
Office = Room("The Front desk of Ethan James High school", "You could talk to the VPs, assistants, and staff", None,
              R19A)
San_Framsico = Room("The City of Rich People AKA San Framsico", "I might need some items in the stores here",  None,
                    Downtown_Dresno)
Cousins_House = Room("My Cousins live here", "They might be of help to me", None, Parents_House)
R13B = Room("Mr. Dawson's Room", "There could be some useful items here", None, SB20, R19A)
SL15 = Room("Mrs. Hazen's Biology Room", "There might be some useful items here", None, R13B, SB20, R19A,)
J_Mart = Room("The J mart to get food, technology, clothing etc.", "I might need some of the useful items here", None,
              Downtown_Dresno, Parents_House)


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
Amphitheater.south = Cafeteria
R19A.west = Amphitheater
R19A.north = parking_lot  # Creates a Key when You type north

# Option 2 - Use strings, but more difficult controller
# R19A = Room("Mr. Wade's Room")
# parking_lot = Room("The Parking Lot", None, R19A)

player = Player(R19A)

directions = ['north', 'south', 'east', 'west', 'southeast', 'northeast']
playing = True

# Controller
while playing:
    print(player.current_location.name)  # The player has a current location and that location has a name
    print(player.current_location.description)  # The player has a current location and that location has a description

    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command in directions:
        try:
            next_room = player.find_room(command)
            if next_room is None:      # If the direction you typed is invalid
                raise KeyError      # Bring up "I can't Go that way"
            player.move(next_room)
        except KeyError:
            print("I can't Go that Way")

    elif "take" in command:
        item = command[5:]  # For the 5th letter the computer will import that item
        item_found = None
        Name = Item
        for item in player.current_location.items:
            if item.name == item:
                item_found = item
            if item_found is not None:
                player.inventory.append(item_found)
                player.current_location.items.remove(item_found)
    else:
        print("Command Not recognized.")

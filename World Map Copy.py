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


class HondaAccord(Sedan):
    def __init__(self):
        super(HondaAccord, self).__init__("HondaAccord")


class ToyotaCamry(Sedan):
    def __init__(self):
        super(ToyotaCamry, self).__init__("ToyotaCamry")


class NissanGTR(Sedan):
    def __init__(self):
        super(NissanGTR, self).__init__("NissianGTR")


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
        self.Cores = 4
        self.virtual_cores = 8


class Cpu3(ComputerParts):
    def __init__(self, name):
        super(Cpu3, self).__init__(name)
        self.Gigahertz = 2.40
        self.Cores = 2
        self.virtual_cores = 2


class Cpu4(ComputerParts):
    def __init__(self, name):
        super(Cpu4, self).__init__(name)
        self.Gigahertz = 8.4           # You'd think that Intel would have the highest clocking CPU, but no its AMD
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
    def __init__(self, name, hd, windows10pro):
        super(HardDrive2, self).__init__(name)
        self.storage = 1000
        self.type = hd
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


class GraphicsCard(ComputerParts):
    def __init__(self, name):
        super(GraphicsCard, self).__init__(name)


class Gtx1050(GraphicsCard):
    def __init__(self, name, good):
        super(Gtx1050, self).__init__(name)
        self.memory = 2
        self.cudacores = 768
        self.power = 300
        self.performance = good


class HD8570(GraphicsCard):
    def __init__(self, name, ok):
        super(HD8570, self).__init__(name)
        self.memory = 1
        self.cudacores = 384
        self.power = 400
        self.performance = ok


class Gtx1070(GraphicsCard):
    def __init__(self, name, excellent):
        super(Gtx1070, self).__init__(name)
        self.memory = 8
        self.cudacores = 2432
        self.power = 500
        self.performance = excellent


class Gtx5010(GraphicsCard):
    def __init__(self, name, outofthisworld):
        super(Gtx5010, self).__init__(name)
        self.memory = 16
        self.cudacores = 50000
        self.power = 1400
        self.performance = outofthisworld


class Gtx1080(GraphicsCard):
    def __init__(self, name, excellent):
        super(Gtx1080, self).__init__(name)
        self.memory = 8
        self.cudacores = 2560
        self.power = 900
        self.performance = excellent


class Rx590(GraphicsCard):
    def __init__(self, name, excellent):
        super(Rx590, self).__init__(name)
        self.memory = 8
        self.cudacores = 2304
        self.power = 700
        self.performance = excellent


class Rx470(GraphicsCard):
    def __init__(self, name, good):
        super(Rx470, self).__init__(name)
        self.memory = 4
        self.cudacores = 2048
        self.power = 500
        self.performance = good


class Rtx2080TI(GraphicsCard):
    def __init__(self, name, advance):
        super(Rtx2080TI, self).__init__(name)
        self.memory = 11
        self.cudacores = 4352
        self.power = 650
        self.performance = advance


class Gtx1660(GraphicsCard):
    def __init__(self, name, excellent):
        super(Gtx1660, self).__init__(name)
        self.memory = 6
        self.cudacores = 1536
        self.power = 450
        self.performance = excellent


class Food(Item):
    def __init__(self, name):
        super(Food, self).__init__(name)


class HamAndCheese(Food):
    def __init__(self, name):
        super(HamAndCheese, self).__init__(name)


class Marshmellows(Food):
    def __init__(self, name):
        super(Marshmellows, self).__init__(name)


class Rice(Food):
    def __init__(self, name):
        super(Rice, self).__init__(name)


class Sushi(Food):
    def __init__(self, name):
        super(Sushi, self).__init__(name)


class Sausages(Food):
    def __init__(self, name):
        super(Sausages, self).__init__(name)


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


GraphicsCard8 = Gtx5010("Aidivn Xforce Gtx5010", outofthisworld=True)
GraphicsCard7 = Rtx2080TI("Aidivn Xforce Rtx 2080TI Founder's Edition", advance=True)
GraphicsCard6 = Rx590("A.N.D Radeon Rx 590", excellent=True)
GraphicsCard5 = Rx470("A.N.D Radeon Rx 470", good=True)
GraphicsCard4 = Gtx1660("Aidivn Xforce Ytx 1660", excellent=True)
GraphicsCard3 = Gtx1080("Aidivn Xforce Ytx 1080 Founder's Edition", excellent=True)
GraphicsCard2 = Gtx1070("Aidivn Xforce Ytx 1070", excellent=True)
GraphicsCard1 = Gtx1050("Aidivn Xforce Ytx 1050", good=True)
PorkAndCheese = HamAndCheese("HamAndCheese")
WhiteSoftCubes = Marshmellows("Marshmellows")
WhiteSeeds = Rice("White Rice")
HotDog = Sausages("Vietnamese Pork Sausages")
RiceAndSeaweed = Sushi("Sushi")
CentralProcessingUnit4 = Cpu4("A.N.D EX-8350")
CentralProcessingUnit3 = Cpu3("Intail Xeon EYE-1623")
CentralProcessingUnit2 = Cpu2("Intail Core EYE7 7700K")
CentralProcessingUnit = Cpu("A.N.D Phenom 2 X4 955")
Computer4 = MotherBoard4("ZombieWare 123Abc Founders Edition Motherboard")
Computer3 = MotherBoard3("Asos X-467 Motherboard")
Computer2 = MotherBoard2("Dull 3746 Motherboard")
Computer1 = MotherBoard("Lanovo S-462 Motherboard")
Ram2 = MemoryFaster("Dinosair DDR4 2400 Megahertz Ram", ddr4=2400)
Ram1 = Memory("Samsong DDR3 1600 Megahertz Ram", ddr3=1600)
SamSong3 = GalaxyS3("Samsong Galaxy Sing3", excellent=True)
SamSong2 = GalaxyS4("Samsong Galaxy Sing4", excellent=True)
SamSong1 = GalaxyS7("Samsong Galaxy Sing7", excellent=True)
Applie = APhone8(APhone8, mint=True)
Toyota = ToyotaCamry()
Nissan = NissanGTR()
Honda = HondaAccord()
hdd = HardDrive("500Gb Samsong Solid State Drive", ssd=500, windows10home=True,)
hdd2 = HardDrive2("Western Analong 2 Tereabyte HardDrive", hd=2000, windows10pro=True,)
hdd3 = HardDrive3("Intel 256gb Solid State Drive", ssd=256, windows10home=True,)
hdd4 = HardDrive4("Samsong 1Tb Solid State Drive", ssd=1000, windows10home=True)


# Option 1 - Use the Variables, but fix later
R19A = Room("Mr. Wade's Room", "This is the room you are in", None, None, None, None, None, None, [hdd3,
            GraphicsCard7, GraphicsCard2, GraphicsCard5, Computer4],)
parking_lot = Room("The Parking Lot", "THere are a few cars parked here", None, R19A, [Toyota], [Nissan], [Honda])
Amphitheater = Room("The stage Outside", "There might be some items here", None, R19A,)
Cafeteria = Room("The Place to get food and chill", "There is some leftover non eaten baked ham and cheese bars and"
                                                    "there might be some items here", None, Amphitheater,
                 [PorkAndCheese], [RiceAndSeaweed], [HotDog], [WhiteSeeds],)
SB20 = Room("Mr Yang's Room", "This guy loves Anime", None, Cafeteria, parking_lot, [WhiteSoftCubes], [Cpu4],
            [GraphicsCard3])
Downtown_Dresno = Room("The City of Dresno", "There are a lot of work offices here", None, parking_lot)
Ethan_James_High_School = Room("Ethan James High School Grades 9-12", "The School", None, Downtown_Dresno)
Grandparents_House = Room("The house that my grandparents live in.", "There could be some items here", None,
                          Ethan_James_High_School, Downtown_Dresno, [hdd], [Computer2], [GraphicsCard4])
Parents_House = Room("My mom, dad, 2 sisters and 1 brother live here", "There could be some helpful items here", None,
                     Grandparents_House, [Ram1], [Cpu2], [Computer3], [GraphicsCard1])
Office = Room("The Front desk of Ethan James High school", "You could talk to the VPs, assistants, and staff", None,
              R19A, [Computer1])
San_Framsico = Room("The City of Rich People AKA San Framsico", "I might need some items in the stores here",  None,
                    Downtown_Dresno, [SamSong3], [SamSong1], [Ram2], [Cpu3], [GraphicsCard8])
Cousins_House = Room("My Cousins live here", "They might be of help to me", None, Parents_House, [Computer2],
                     [SamSong2])
R13B = Room("Mr. Dawson's Room", "There could be some useful items here", None, SB20, R19A, [Cpu3], [APhone8])
SL15 = Room("Mrs. Hazen's Biology Room", "There might be some useful items here", None, R13B, SB20, R19A, [APhone10F])
J_Mart = Room("The J mart to get food, technology, clothing etc.", "I might need some of the useful items here", None,
              Downtown_Dresno, Parents_House, [hdd4], [GraphicsCard6], [Cpu])


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
player.inventory.append(Item)

directions = ['north', 'south', 'east', 'west', 'southeast', 'northeast']
short_directions = ['n', 's', 'e', 'w', ]

playing = True

# Controller
while playing:
    print(player.current_location.name)  # The player has a current location and that location has a name
    print(player.current_location.description)  # The player has a current location and that location has a description
    print()
    print("The following items are in the room:")
    for item in player.current_location.items:
        print(item.name)

    command = input(">_")

    if command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]

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
        for item in player.current_location.items:    # For the Item in the player's current location
            if item.name == item:           # If the item name is shown
                item_found = item       # The item is show
            if item_found is not None:
                player.inventory.append(item_found)
                player.current_location.items.remove(item_found)
    else:
        print("Command Not recognized.")

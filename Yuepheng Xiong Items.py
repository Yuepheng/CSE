class Item(object):
    def __init__(self, name):
        self.name = name


class ModeOfTransportation(object):
    def __init__(self, name):
        self.name = name


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


class NissianGTR(Sedan):
    def __init__(self):
        super(NissianGTR, self).__init__("NissianGTR")

    def starting_the_engine(self):
        self.engine_on = False
        print("I started the GTR by stepping on the brake and pushing the start button")


NineteenNinetyNine = HondaAccord()
NineteenNinetyNine.amount_of_oil()
NineteenNinetyNine.the_battery_supplying_to_starter()
NineteenNinetyNine.amount_of_fuel()
NineteenNinetyNine.starting_the_engine()

NineteenNinetySix = ToyotaCamry()
NineteenNinetySix.amount_of_fuel()
NineteenNinetySix.starting_the_engine()

TwoThousandEightTeen = NissianGTR()
TwoThousandEightTeen.amount_of_fuel()
TwoThousandEightTeen.starting_the_engine()


class Case(object):
    def __init__(self, name):
        self.name = name


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


class Computerparts(object):
    def __init__(self, name):
        self.name = name


class AcPowerSupply(Computerparts):
    def __init__(self, name):
        super(AcPowerSupply, self).__init__(name)
        self.name = name
        self.Watts = 500


class Cpu(Computerparts):
    def __init__(self, name):
        super(Cpu, self).__init__(name)
        self.name = name
        self.Gigahertz = 3.20
        self.Cores = 4
        self.virtual_cores = 4


class MotherBoard(Computerparts):
    def __init__(self, name):
        super(MotherBoard, self).__init__(name)
        self.name = name
        self.cpu_slot = True
        self.ram_slots = 4
        self.Pcix16 = True
        self.power_supply_connector = True
        self.hard_drive_connector_wires = True


class Memory(Computerparts):
    def __init__(self, name, ddr3):
        super(Memory, self).__init__(name)
        self.name = name
        self.type = ddr3
        self.amount = 12
        self.speed = 1600


class HardDrive(Computerparts):
    def __init__(self, name, ssd, windows10home):
        super(HardDrive, self).__init__(name)
        self.storage = 500
        self.type = ssd
        self.speed = 300
        self.os = windows10home


class PowerSupply(Computerparts):
    def __init__(self, name, ac, generic):
        super(PowerSupply, self).__init__(name)
        self.power = 500
        self.type = ac
        self.size = generic


class PhoneBrand(object):
    def __init__(self, name):
        self.name = name


class Applie(PhoneBrand):
    def __init__(self, name):
        super(Applie, self).__init__(name)
        self.name = name


class SamSong(PhoneBrand):
    def __init__(self, name):
        super(SamSong, self).__init__(name)
        self.name = name


class GalaxyS4(SamSong):
    def __init__(self, name, excellent):
        super(GalaxyS4, self).__init__(name)
        self.name = name
        self.storage = 16
        self.os = 4.4
        self.camera = 13
        self.condition = excellent


class GalaxyS3(SamSong):
    def __init__(self, name, excellent):
        super(GalaxyS3, self).__init__(name)
        self.name = name
        self.storage = 32
        self.os = 4.2
        self.camera = 8
        self.condition = excellent


class GalaxyS7(SamSong):
    def __init__(self, name, excellent):
        super(GalaxyS7, self).__init__(name)
        self.name = name
        self.storage = 64
        self.os = 7
        self.camera = 14
        self.condition = excellent


class APhone8(Applie):
    def __init__(self, name, mint):
        super(APhone8, self).__init__(name)
        self.name = name
        self.storage = 64
        self.os = 12
        self.camera = 13
        self.condition = mint


class APhone10F(Applie):
    def __init__(self, name, good):
        super(APhone10F, self).__init__(name)
        self.name = name
        self.storage = 128
        self.os = 12
        self.camera = 15
        self.condition = good

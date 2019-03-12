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
        super(Case, self).__init__(name)
        self.size = 48
        self.ram_slots = 4
        self.power_supply = None
        self.hard_drive = None
        self.motherboard = True

    def how_big_the_case_is(self):
        self.size = 48
        print("The Case is 48 cm long.")

    def the_slots_that_ram_could_be_put_in(self):
        self.ram_slots = 4
        print("There are four DDR3 1600 megahertz ram slots that I could put the ram in")

    def the_power_supply(self):
        self.power_supply = None
        print("Hmmmm There's No Power Supply.... Guess I'll have to go looking for one that goes with the GTX 1060")

    def the_hard_drive_or_ssd(self):
        self.hard_drive = None
        print("Ok It has no Hard drive either, I could go with an SSD, but I'm on a Budget here.")

    def the_motherboard(self):
        self.motherboard = None
        print("At least It has a motherboard, although it is an OEM motherboard, might not be good for overclocking")


class HdPavalionDesktop(HdCase):
    def __init__(self):
        super(HdPavalionDesktop, self).__init__("HdPavalionDesktop")


Pavalion = HdPavalionDesktop
Pavalion.size()
Pavalion.ram_slots()

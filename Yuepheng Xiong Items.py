class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, name, damage):
        super(Weapon, self).__init__(name)
        self.damage = damage


class Armor(Item):
    def __init__(self, name, armor_amt):
        super(Armor, self).__init__(name)
        self.armor_amt = armor_amt


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

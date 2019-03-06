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


NineteenNinetyNine = HondaAccord()
NineteenNinetyNine.Oil_Level()
NineteenNinetyNine.fuel_level()
NineteenNinetyNine.battery_voltage()

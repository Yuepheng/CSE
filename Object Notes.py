class Laptop(object):
    def __init__(self, screen_resolution, extra_space=1000, colour="Cobalt"):
        # THings that a Laptop has.
        # Everything in this list should relevant to the program.
        self.processor = "Intel i5"
        self.screen_resolution = screen_resolution
        self.battery_left = 100
        self.space_left = extra_space
        self.color = colour
        self.os = "Linux"
        self.functioning = True

    def charge(self, time):
        if self.functioning:
            # Computer is already charged
            if self.battery_left >= 100:
                print("The Computer is already charged")
                return

            self.battery_left += time  # This adds to the battery life
            # Computer is Mostly Charged
            if self.battery_left > 100:
                print("The Computer quickly charges.")
                self.battery_left = 100

            # Computer is not charged at all
            else:
                print("The computer is now at %d%%" % self.battery_left)
        else:
            print("It's Broken. Good Job")

    def smash(self):
        self.functioning = False
        print("I took the laptop")
        print()
        print()
        print()
        print("...AND I THREW IT ON THE GROUND")

    def use(self, time):
        self.battery_left -= time
        print("You used the laptop for %s minutes" % time)


my_computer = Laptop("1920x1080", 10000, "Black")
your_computer = Laptop('10x10', 10, "Orange")
wiebe_computer = Laptop("90000000000x9000000000", 999999999999999999, "Awesome")
default_computer = Laptop("1920x1080")

my_computer.use(60)
my_computer.charge(20)
my_computer.charge(1000)
my_computer.smash()
my_computer.charge(20)

your_computer.charge(20)

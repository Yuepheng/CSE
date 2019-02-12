class Laptop(object):
    def __init__(self, screen_resolution, extra_space, colour):
        # THings that a Laptop has.
        # Everything in this list should relevant to the program.
        self.processor = "Intel i5"
        self.screen_resolution = screen_resolution
        self.battery_left = 100
        self.space_left = extra_space
        self.color = colour
        self.os = "Linux"

    def charge(self, time):
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


my_computer = Laptop("1920x1080", 10000, "Black")
your_computer = Laptop('10x10', 10, "Orange")
wiebe_computer = Laptop("90000000000x9000000000", 999999999999999999, "Awesome")
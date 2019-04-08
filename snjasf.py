class Item(object):
    def __init__(self, name):
        self.name = name


class Computerparts(Item):
    def __init__(self, name):
        super(Computerparts, self).__init__(name)


class HardDrive(Computerparts):
    def __init__(self, name, hdd, windows10pro):
        super(HardDrive, self).__init__(name, hdd, windows10pro)


HardDrive1 = HardDrive("eye 32134", "HardDiskDrive", "windows10Pro")

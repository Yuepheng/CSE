class Pencil(object):
    def __init__(self):
        self.delete = "Eraser"
        self.material = "Wood"
        self.stuff_inside = 100
        self.color = "Yellow"
        self.Brand = "DIXON TACONDERAGA"
        self.stuff_inside = True

    def marking(self, write):
        if self.stuff_inside:
            if self.stuff_inside >= 100:
                print("It doesn't need to be sharpened.")
                return

            self.stuff_inside += write
            if self.stuff_inside > 100:
                print("I'm sharpening the pencil so I can write")
                self.stuff_inside = 100

            else:
                print("Alright, I'm sure this will be useful later...")

    def wear(self):
        self.stuff_inside = False
        print("Looks like I need to sharpen the pencil")
        print("There. It's sharp.")

    def eraser(self):
        self.stuff_inside -= 100
        print("Well this looks like its at a %s percentage of wear before I need to sharpen it." % 100)


test = Pencil()
test.marking(15)
test = Pencil()
test.wear()
test = Pencil()
test.eraser()

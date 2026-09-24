class Glassware:
    def __init__(self, material):
        self.material = material

class Beaker(Glassware):
    def __init__(self, material, capacity):
        super().__init__(material)
        self.capacity = capacity

class Tray:
    def __init__(self):
        self.beaker1 = Beaker("Glass", 100)
        self.beaker2 = Beaker("Glass", 100)
        self.beaker3 = Beaker("Glass", 100)
        self.beaker4 = Beaker("Glass", 100)
        self.beaker5 = Beaker("Glass", 100)

tray = Tray()

print("Tray contains 5 beakers.")
print("Beaker 1:", tray.beaker1.capacity, "mL")
print("Beaker 2:", tray.beaker2.capacity, "mL")
print("Beaker 3:", tray.beaker3.capacity, "mL")
print("Beaker 4:", tray.beaker4.capacity, "mL")
print("Beaker 5:", tray.beaker5.capacity, "mL")

del tray

print("The tray is deleted, the 5 beakers is now gone"

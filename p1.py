class Car:

    wheel = 4

    def __init__(self,brand,model,colour):
        self.Brand = brand
        self.Model = model
        self.Colour = colour

    def viewDisplay(self):
        print("Name ",self.Brand)
        print("Model ",self.Model)
        print("Colour ",self.Colour)
        print("Wheel ",Car.wheel)

    
c1 = Car("BMW-4","BMW-2026","White")
c2 = Car("Audi","Audi-2026","Brown")

c1.viewDisplay()
c2.viewDisplay()
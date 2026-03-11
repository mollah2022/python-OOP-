class Car:

    wheel = 4

    def __init__(self,name,colour):
        self.Name = name
        self.Colour = colour

    def display(self):
        print("Name ",self.Name)
        print("Colour ",self.Colour)
        self.displayClassVariable()

    @classmethod
    def displayClassVariable(cls):
        print("Wheel ",cls.wheel)

    
    @staticmethod
    def hudaiFunction():
        print("Hello Car Class ")

    
c1 = Car("BMW","Pink")
c2 = Car("Audi","Brown")

c1.display()
c2.display()
c1.hudaiFunction()
c2.hudaiFunction()
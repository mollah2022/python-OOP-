#####################################################WithOut super function()#######################################
####################################################################################################################
class Animal:

    def __init__(self,name,colour):
        self.Name = name
        self.Colour = colour

    def viewDetails(self):
        print("Name ",self.Name)
        print("Colour ",self.Colour)

class Dog(Animal):

    def sound(self):
        print("Dog Sound")
        
d1 = Dog("Rover","Black")
d1.viewDetails()
d1.sound()

######################################################################################################
########################## With Super Function()######################################################

class Animal:

    def __init__(self,name,colour):
        self.Name = name
        self.Colour = colour

    def viewDetails(self):
        print("Name ",self.Name)
        print("Colour ",self.Colour)

class Dog(Animal):

    def __init__(self,name,colour,leg):
        super().__init__(name,colour)
        self.Leg = leg

    def sound(self):
        print("Leg ",self.Leg)
        print("Dog Sound")
        
d1 = Dog("Rover","Black",4)
d1.viewDetails()
d1.sound()
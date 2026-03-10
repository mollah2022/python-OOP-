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

class Cat(Animal):

    def soundc(self):
        print("Cat Sound")

############## Two Obejct access in Class One ###########################
        
d1 = Dog("Rover","Black")
d1.viewDetails()
d1.sound()

#################################################

c1 = Cat("Monkey","Red")
c1.viewDetails()
c1.soundc()
class Animal:

    def sound(self):
        print("Animal Sound")
    
class Dog:
    
    def sound(self):
        print("DOG sound")

class Cat:

    def sound(self):
        print("Cat sound")

class Rat:

    def sound(self):
        print("Rat sound")

overall = [Animal(),Cat(),Dog(),Rat()]

for x in overall:
    x.sound()
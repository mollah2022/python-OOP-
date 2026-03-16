class Animal:
    def sound(self):
        print("Animal Sound")
    
class Dog(Animal):
    def sound(self):
        print("______________++++++++++++++++++++++++++++++__________________________")
        super().sound()   # <-- parentheses লাগবে
        print("DOG sound")

class Cat(Animal):
    def sound(self):
        print("______________++++++++++++++++++++++++++++++__________________________")
        super().sound()
        print("Cat sound")

class Rat(Animal):
    def sound(self):
        print("______________++++++++++++++++++++++++++++++__________________________")
        super().sound()
        print("Rat sound")


overall = [Animal(), Cat(), Dog(), Rat()]

for x in overall:
    x.sound()

print("\nSingle Dog call:")
d1 = Dog()
d1.sound()

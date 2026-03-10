class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def bark(self):
        print("Dog bark")

class Cat(Animal):
    def meow(self):
        print("Cat meow")

class Baby(Dog, Cat):
    def play(self):
        print("Baby playing")

b = Baby()
b.sound()
b.bark()
b.meow()
b.play()

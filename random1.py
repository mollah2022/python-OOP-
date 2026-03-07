class Dog:

    def __init__(self,name,color):
        self.name = name
        self.color = color

    def update(self,color):
        self.color = color

    def view(self):
        print(self.color," ",self.name," ","is smalling")

#================================================================================

d1 = Dog("Rover","Brown")
d2 = Dog("Toomy","White")

print("Before Update Value -----------------===============================-----------------------")

d1.view()
d2.view()

d1.update("Black")
d2.update("Pink")

print("After Update ------------------------=============================----------------------------")

d1.view()
d2.view()

print("Dict Value -----------------------------------=========================================--------------------------")

print("First obejct ",d1.__dict__)
print("Second obejct ",d2.__dict__)

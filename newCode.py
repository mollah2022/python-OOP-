class Car:

    def __init__(self,brand,color):
        self.wheel = 4
        self.Brand = brand 
        self.color = color

        print("Wheel ------->>>>>>> ",self.wheel)

    def view(self):
        print("Brand --->>>>> ",self.Brand)
        print("Colour --->>>> ",self.color)



c1 = Car("BMW","Red")
c2 = Car("Audi","White")

c1.view()
c2.view()
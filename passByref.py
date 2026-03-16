
class Cat:

    def __init__(self,color,action):
        self.color = color
        self.action = action

    def view(self):
        print("Color ",self.color)
        print("Action ",self.action)

    
    def compare(self,reciveObject):
        if self.action == reciveObject.action:
            print("Both are same ",self.action)
        else:
            print("They are not same")
        
    

c1 = Cat("Black","Jumping")
c2 = Cat("Red","Jumping")
c3 = Cat("pink","Swimming")

c1.view()
c2.view()
c3.view()

c1.compare(c2)
c2.compare(c3)
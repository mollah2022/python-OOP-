class House:

    def __init__(self):
        self.window = 6
        self.door = 3

    def views(self):
        print(self.window," Windos",self.door," Doors")



hs1 = House()
hs1.window = 10
hs1.door = 5

hs1.views()

hs2 = House()
hs2.window = 20
hs2.door = 7

hs2.views()
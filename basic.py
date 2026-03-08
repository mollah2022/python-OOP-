class Students:

    def __init__(self,name,id):
        self.Name = name
        self.Id = id
        print("Hello INIT VAI-------")
        
    def display(self):
        print("Name ",self.Name,"ID ",self.Id)

std1 = Students("sajib",23)
std1.display()
std2 = Students("tamim",98)
std2.display()
class Cal:

    def __init__(self,name=None,age=None,gender=None):
        self.Name = name
        self.Age = age
        self.Gender = gender
        
    def viwes(self):
        print("name",self.Name,"Age",self.Age,"Gender",self.Gender)

c1 = Cal()
c2 = Cal("sajib")
c3 = Cal("Sajib","23")
c4 = Cal("sajib",23,"male")

c1.viwes()
c2.viwes()
c3.viwes()
c4.viwes()
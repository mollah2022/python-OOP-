class Student:

    uni_Name = "BUBT"

    def __init__(self,name,id):
        self.Name = name
        self.Id = id

    def display(self):
        print("My Name is ",self.Name)
        print("My Id is a ",self.Id)
        print("My University Name is ",Student.uni_Name)

    @classmethod
    def Creating_factor_method(cls,WantName):
        Name,Id = WantName.split('-')
        newBoject = cls(Name,Id)
        return newBoject
    

s1 = Student("Rakib",456)
s2 = Student.Creating_factor_method("Sajib-53")

s1.display()
s2.display()

#amra classmethod dia obejct er bitore value dilam akbre alada alda na dia pore split kore alada korlam......
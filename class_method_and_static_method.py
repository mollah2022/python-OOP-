class Student:

    uni_name = "BUBT"

    def __init__(self,name,id):
        self.Name = name
        self.__Id = id

    def view(self):
        print("Name ",self.Name)
        print("ID ",self.__Id)
        print("UN_NAME ",Student.uni_name)

    #static_Method::: self ba cls kichui nibe na
    @staticmethod
    def display():
        print("We ar BUBTian Gays")

    @classmethod
    def update_uni_name(cls,updateName):
        cls.uni_name = updateName


s1 = Student("SAJIB AHMED",53)
Student.update_uni_name ("Bangladesh University and Business and Techonology")
s1.view()
s1.display()

    
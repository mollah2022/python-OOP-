
class Student:

    def __init__(self,name,id):
        self.name = name
        self.__id = id

    def view(self):
        print("Name",self.name)
        print("ID",self.__id)
        self.__display()
        

    def set_id(self,id):
        if id > 0:
            self.__id = id
        else:
            print("Error ID")
    def get_id(self):
        return self.__id
    
    def __display(self):
        print("Hello Private Method")
    

std1 = Student("sajib",23)
std2 = Student("Rakib",99)

std1.view()
std2.view()

std1.set_id(20)
std1.view()
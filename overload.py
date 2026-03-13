from typing import overload

class Student:

    def __init__(self):
        print("Hello World")

    @overload
    def add(self, num1: int, num2: int) -> None: ...
    
    @overload
    def add(self, num1: int, num2: int, num3: int) -> None: ...
    
    @overload
    def add(self, str1: str, str2: str) -> None: ...

    def add(self, *args):
        if len(args) == 2 and isinstance(args[0], int):
            print(args[0] + args[1])

        elif len(args) == 3:
            print(args[0] + args[1] + args[2])

        elif len(args) == 2 and isinstance(args[0], str):
            print("My Name is", args[0], args[1])


s1 = Student()

s1.add(1,2)
s1.add(2,3,4)
s1.add("sajib","ahmed")

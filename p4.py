from typing import overload
class Cal:

    def __init__(self):
        pass

    
    @overload
    def add(self,num1:int,num2:int) -> None: ...

    @overload
    def add(self,num1:int,num2:int,num3:int) -> None: ...

    @overload
    def add(self,num1:int,num2:int,num3:int,num4:int) -> None: ...


    def add(self, *args):
        if len(args) == 2 and isinstance(args[0], int):
            print(args[0] + args[1])

        elif len(args) == 3:
            print(args[0] + args[1] + args[2])
        else:
             print(args[0] + args[1] + args[2]+args[3])


c1 = Cal()
c1.add(1,2)
c1.add(1,2,3)
c1.add(1,2,3,4,5)
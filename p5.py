class Object:

    def __init__(self,Number):
        self.Number = Number

    def __add__(self, other):
        sum = self.Number+other.Number
        print(sum)




c1 = Object(5)
c2 = Object(4)
c1+c2
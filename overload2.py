from oop.book import __init__

class Calculator:

    def __init__(self,x):
        self.x = x

    def __gt__(self, other):
        if self.x > other.x:
            return "cal1 is high than cal2"


cal1 = Calculator(5)
cal2 = Calculator(3)

print(cal1 > cal2)

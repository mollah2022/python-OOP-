class Cat:

    def __init__(self,color,action):
        self.color = color
        self.action = action

    def view(self,nums,clr):
        clr1 = clr
        nums = nums + 15
        clr1[0] = "OffWhite"

        print(nums)
        print(clr1)


c1 = Cat("RED","Sleeping")

colors = ["Green","White","Yellow","Pink","Brown"]
number = 65

c1.view(number,colors)

print("Object call er pore --------========================---------------")

print(colors)
print(number)
class A:

    def __init__(self):
        pass 

    def display1(self):
        print("Hello A class")

class B:

    def displayb(self):
        print("Hello class B") 

class C(A,B):

    def displayc():
        print("Hello C class ")

c1 = C()
c1.display1()
c1.displayb()
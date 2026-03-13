from Creating_Factory_Method import display
class AAAAAA:

    def __init__(self):
        pass 
    

    def displayA(self):
        print("Print Hello Class AAAAAA")
    
class BBBBBB(AAAAAA):

    def displayB(self):
        print("Print Hello Class BBBBBB")

class CCCCCC(BBBBBB):

    def displayC(self):
        print("Print Hello Class CCCCCC")

######## a1 obejct of AAAAAA class so a1 access in displaya()##############
    
a1 = AAAAAA()
a1.displayA()

############### b1 obejct of BBBBBB class so b1 access in displab() and BBBBBB class inherit class AAAAAA so b1 access in displaya() ############

b1 = BBBBBB()
b1.displayA()
b1.displayB()

############### Same Way c1 access in displaya(),displayb() and displayc()############

c1 = CCCCCC()
c1.displayA()
c1.displayB()
c1.displayC()
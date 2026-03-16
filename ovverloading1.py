
class Calculator:

    def multiply(self,num1,num2):
        print(num1*num2)


    def multiply(self,*nums):
        sum = 0
        for x in nums:
            sum+=x
        print(sum)

cal1 = Calculator()

cal1.multiply(2,3)
cal1.multiply(3,4,5)
cal1.multiply(1,2,3,4,5,6)
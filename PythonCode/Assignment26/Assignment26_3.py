class Airthmatic:
    def __init__(self):
        self.value1 = 0
        self.value1 = 0
    def Accept(self):
        self.value1 = float(input("enter the first number : "))
        self.value2 = float(input("enter the second number : "))
    def addition(self):
        return self.value1+self.value2
    def subtraction(self):
        return self.value1-self.value2
    def multipecation(self):
        return self.value1*self.value2
    def division(self):
        try:
         ans = self.value1/self.value2
         return ans
        except ZeroDivisionError as zobj:
            print("ZeroDivisionError exception")
        

aobj1 = Airthmatic()
aobj1.Accept()
print("Addition is : ",int(aobj1.addition()))
print("subtravtion is : ",int(aobj1.subtraction()))
print("multiplication is : ",int(aobj1.multipecation()))
print("division is : ",int(aobj1.division()))


aobj2 = Airthmatic()
aobj2.Accept()
print("Addition is : ",int(aobj2.addition()))
print("subtravtion is : ",int(aobj2.subtraction()))
print("multiplication is : ",int(aobj2.multipecation()))
print("division is : ",int(aobj2.division()))


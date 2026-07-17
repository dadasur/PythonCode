class Demo:
    value = 10
    def __init__(self,a,b):
        self.no1 = a
        self.no2 = b
    def fun(self):
        print(self.no1,self.no2)
    def gun(self):
        print(self.no1,self.no2)

obj1 = Demo(11,21)
obj2 = Demo(51,101)
obj1.fun()
obj1.fun()
obj2.gun()
obj2.gun()
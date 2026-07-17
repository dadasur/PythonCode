class Circle:
    PI = 3.14
    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0
    def Accept(self):
        self.Radius = float(input("enter radious : "))
    def CalculateAreaofCircle(self):
        self.area = Circle.PI * (self.Radius*self.Radius)
    def CalculateAreaofCircumference(self):
        self.Circumference = 2 * Circle.PI * (self.Radius*self.Radius)
    def Display(self):
        print("Radius is : ", self.Radius)
        print("Area of circle is  : ",self.area)
        print("Area of circunmference is : ",self.Circumference)

aobj1 = Circle()
aobj1.Accept()
aobj1.CalculateAreaofCircle()
aobj1.CalculateAreaofCircumference()
aobj1.Display()
       
aobj2 = Circle()
aobj2.Accept()
aobj2.CalculateAreaofCircle()
aobj2.CalculateAreaofCircumference()
aobj2.Display()
           

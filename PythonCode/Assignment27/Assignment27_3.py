class Numbers:
    def __init__(self,a):
        self.No = a
    def Display(self):
        print("accunt name :", self.Name)
        print("current balance :", self.Amount)

    def CheckPrime(self):
         if self.No <= 1:
          return False
         for i in range(2,int(self.No),1):         
          if self.No%i==0:
           return False
         return True
    
    def CheckPerfect(self):
        sum = 0
        for i in range(1,self.No,1):
         if self.No%i==0:
            sum = sum + i
        if sum == self.No:
           return True
        else:
           return False    
        
    def Factors(self): 
        res = []       
        for i in range(1,self.No,1):
         if self.No%i==0:
            res.append(i)
        return res
    def SumFactors(self):        
        res = 0     
        for i in range(1,self.No,1):
         if self.No%i==0:
            res = res + i
        return res


obj1 = Numbers(6)

if obj1.CheckPrime():
   print(f"{obj1.No} it is a prime number")
else:
   print(f"{obj1.No} it is a not prime number")

if obj1.CheckPerfect():
   print(f"{obj1.No} it is is a perfect number")
else:
   print(f"{obj1.No} it is is not a perfect number")


print("factor is : ",obj1.Factors())
print("sum of factor is : ",obj1.SumFactors())



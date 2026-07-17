class BankAccount:
    ROI = 10.5
    def __init__(self,a,b):
        self.Name = a
        self.Amount = b
    def Display(self):
        print("accunt name :", self.Name)
        print("current balance :", self.Amount)

    def Diposit(self):
        no = int(input("enter Diposit amount : "))
        self.Amount = self.Amount + no
    def Withdraw(self):
        no = int(input("enter Withdraw amount : "))
        self.Amount = self.Amount - no
    def CalculateRateOfIntrest(self):        
        return (self.Amount * BankAccount.ROI)/100 


obj1 = BankAccount("pravin",10000)
obj1.Display()
obj1.Diposit()
obj1.Display()
obj1.Withdraw()
obj1.Display()
print("rate of inteset is : ", obj1.CalculateRateOfIntrest())

obj2 = BankAccount("Rahul",20000)
obj2.Display()
obj2.Diposit()
obj2.Display()
obj2.Withdraw()
obj2.Display()
print("rate of inteset is : ", obj2.CalculateRateOfIntrest())


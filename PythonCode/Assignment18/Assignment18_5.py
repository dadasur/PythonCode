import MarvellousNum
def ListPrime(Data):
    sum = 0
    for i in Data:        
        if MarvellousNum.CheckPrime(i):
            sum = sum + i
    return sum
     
def main():
    
     n = input("Enter All N Number sepreated by space : ")
     values = []
     for i in n.split():
            values.append(int(i))
     ret = ListPrime(values)
     print("Addition of prime NUmber is",ret)
  
if __name__ == "__main__":
    main()
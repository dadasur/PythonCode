import threading

def checkprime(No):
     if No <= 1:
      return False       
     for i in range(2,int(No),1):
        if No%i==0:
            return False
     return True

def checknonprime(No):    
      for i in range(2,int(No),1):
        if No%i==0:
            return False
     

def checkDataofPrime(Data1):
    Resultt = []
    for i in Data1:
       if checkprime(i):
          Resultt.append(i)
    print(f"primary  number are {Resultt} thread id is : {threading.get_ident()}")

def checkDataofNonPrime(Data1):
    Result = []
    for i in Data1:
       if checknonprime(i) == False:
          Result.append(i)
    print(f"not primary  number are {Result} thread id is : {threading.get_ident()}")
           
def main():
    values = [1,2,3,4,5,6,7,8,9,10]
    print(f"main thread id is : {threading.get_ident()}")
    t1 = threading.Thread(target=checkDataofPrime,args=(values,))
    t2 = threading.Thread(target=checkDataofNonPrime,args=(values,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == "__main__":
    main()
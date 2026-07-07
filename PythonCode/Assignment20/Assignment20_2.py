import threading

def CheckEven(no):
    Result = []
    sum = 0
    for i in range(1,no+1):
        if i%2==0:
         for j in range(1,i+1):
          if i%j==0:          
           Result.append(int(j))
    for i in Result:
       sum = sum + i
    print(f"sumation of even factor {sum} thread id is : {threading.get_ident()}")

def CheckOdd(no1):
    OddResult = []
    sumodd = 0
    for ii in range(1,no1+1):
        if ii%2!=0:
         for jj in range(1,ii+1):
          if ii%jj==0:          
           OddResult.append(int(jj))
    
    for k in OddResult:
       sumodd = sumodd + k
    print(f"sumation of odd factor {sumodd} thread id is : {threading.get_ident()}")

def main():
    print(f"main thread id is : {threading.get_ident()}")
    t1 = threading.Thread(target=CheckEven,args=(10,))
    t2 = threading.Thread(target=CheckOdd,args=(10,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == "__main__":
    main()
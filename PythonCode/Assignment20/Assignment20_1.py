import threading

def CheckEven(no):
    Result = []
    for i in range(1,no+1):
        if i%2==0:         
         Result.append(i)
    print(f"even number are {Result} thread id is : {threading.get_ident()}")
def CheckOdd(no):
    Result = []
    for i in range(1,no+1):
        if i%2!=0:         
         Result.append(i)
    print(f"odd number are {Result} thread id is : {threading.get_ident()}")
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
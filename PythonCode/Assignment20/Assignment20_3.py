import threading

def CheckEven(Data1):
    Result = []
    sum = 0
    for i in Data1:
        if i%2==0:         
         sum = sum + i
    print(f"even number sum are {sum} thread id is : {threading.get_ident()}")
def CheckOdd(Data2):
    oddsum = 0
    for j in Data2:
        if j%2!=0:         
         oddsum = oddsum + j
    print(f"odd number sum are {oddsum} thread id is : {threading.get_ident()}")
def main():
    Values = [1,2,3,4,5,6,7,8,9,10]
    print(f"main thread id is : {threading.get_ident()}")
    t1 = threading.Thread(target=CheckEven,args=(Values,))
    t2 = threading.Thread(target=CheckOdd,args=(Values,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == "__main__":
    main()
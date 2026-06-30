
def Perfect(No1):
    sum = 0
    for i in range(1,No1,1):
        if No1%i==0:
            sum = sum + i
    return sum
    
def main():
    value1 = int(input("enter Number : "))
    ret = Perfect(value1)
    if(ret == value1):
        print("Yes It is Perfect Numbre")
    else:
        print("No, it is not Perfect number")
     
if __name__ == "__main__":
    main()

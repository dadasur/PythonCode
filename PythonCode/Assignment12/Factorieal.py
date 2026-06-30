
def Factorial(No):
    Result = []
    for i in range(1,No+1,1):
        if No%i==0:
            Result.append(i)
    return Result
    

def main():
    value = int(input("enter one number : "))
    ret = Factorial(value)
    print(ret)
    
if __name__ == "__main__":
    main()

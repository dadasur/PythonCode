
def PrintManyNumber(No):
    Result = []
    for i in range(1,No+1,1):
            Result.append(i)
    return Result
    

def main():
    value = int(input("enter one number : "))
    
    ret = PrintManyNumber(value)
    print(ret)
    
if __name__ == "__main__":
    main()

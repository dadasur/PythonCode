def CheckOdd(No):
    Result = []
    for i in range(1,No+1,1):
        if i%2!=0:
            Result.append(i)
    return Result
    
    
def main():
    value1 = int(input("Enter the Number"))
    ret = CheckOdd(value1)
    print(ret)

if __name__ == "__main__":
    main()
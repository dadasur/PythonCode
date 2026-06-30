def MultiplicationTable(No):
    Result = []
    for i in range(1,11,1):
        No1 = No*i
        Result.append(No1)
    return Result
    
    
def main():
    value1 = int(input("Enter the Number"))
    ret = MultiplicationTable(value1)
    print(ret)

if __name__ == "__main__":
    main()
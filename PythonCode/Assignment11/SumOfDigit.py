def SumOfDigit(No):
    Result = 0
    while int(No) > 0:
        digit = int(No) % 10
        No =int(No)/10
        Result = Result + digit      
    return Result

def main():
    value1 = int(input("Enter the Number"))
    ret = SumOfDigit(value1)
    print("addition of digit is : ",ret)
    
if __name__ == "__main__":
    main()
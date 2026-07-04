LambdaAddition = lambda No1,No2: (No1+No2)
    
    
def main():
    value1 = int(input("Enter firstthe Number"))
    value2 = int(input("Enter second Number"))
    ret = LambdaAddition(value1,value2)
    print("addition is",ret)

if __name__ == "__main__":
    main()
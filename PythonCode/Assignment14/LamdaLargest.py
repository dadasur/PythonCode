LambdaLargest = lambda No1,No2,No3: No1 if(No1>=No2) and (No1>=No3) else No2 if(No2>=No1) and (No2>=No3) else No3
    
    
def main():
    value1 = int(input("Enter firstthe Number"))
    value2 = int(input("Enter second Number"))
    value3 = int(input("Enter Thrid Number"))
    ret = LambdaLargest(value1,value2,value3)
    print("largest is",ret)

if __name__ == "__main__":
    main()
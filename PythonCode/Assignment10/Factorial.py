def Factorial(No):
    for i in range(1,No,1):
        No = No*i
    return No
    
    
def main():
    value1 = int(input("Enter the Number"))
    ret = Factorial(value1)
    print(ret)

if __name__ == "__main__":
    main()
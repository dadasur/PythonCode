def CountOfDigit(No):
    Counter = 0
    while int(No) > 0:
        No =int(No)/10
        Counter = Counter +1        
    return Counter
    
    
def main():
    value1 = int(input("Enter the Number"))
    ret = CountOfDigit(value1)
    print(ret)
    
if __name__ == "__main__":
    main()
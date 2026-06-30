def ReverseOfDigit(No):
    reverse = 0
    while int(No) > 0:
        digit = int(No) %10
        No =int(No)/10
        reverse = reverse * 10 + digit
    return reverse
    
    
def main():
    value1 = int(input("Enter the Number"))
    ret = ReverseOfDigit(value1)
    print(ret)
    
if __name__ == "__main__":
    main()
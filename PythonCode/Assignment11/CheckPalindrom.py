def Palindrom(No):
    reverse = 0
    while int(No) > 0:
        digit = int(No) %10
        No =int(No)/10
        reverse = reverse * 10 + digit
    return reverse
    
    
def main():
    value1 = int(input("Enter the Number"))
    ret = Palindrom(value1)
    if ret == value1:
        print("Yes, it is palindrom")
    else:
        print("NO. it is not palindrom")
    
if __name__ == "__main__":
    main()
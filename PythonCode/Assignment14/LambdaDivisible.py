Divisible = lambda No: True if(No%5==0) else False
    
    
def main():
    value1 = int(input("Enter the Number"))
    ret = Divisible(value1)
    if ret == True:
        print("Yes, it is divisible by 5",ret)
    else:
        print("No, it is not divisible by 5",ret)

if __name__ == "__main__":
    main()
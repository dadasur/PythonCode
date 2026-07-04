CheckOdd=lambda No : True if No%2!=0  else False
        
def main():
    value1 = int(input("Enter the Number"))
    ret = CheckOdd(value1)
    if ret == True:
        print("NUmber is odd",ret)
    else:
        print("NUmber is odd",ret)

if __name__ == "__main__":
    main()
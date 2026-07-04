CheckEven=lambda No : True if No%2==0  else False
        
def main():
    value1 = int(input("Enter the Number"))
    ret = CheckEven(value1)
    if ret == True:
        print("NUmber is even",ret)
    else:
        print("NUmber is even",ret)

if __name__ == "__main__":
    main()
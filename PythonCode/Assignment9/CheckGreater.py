def ChkGreate(No1,No2):
    if No1 > No2:
        return No1
    elif No2 > No1:
        return No2
    
def main():
    value1 = int(input("Enter the first Number"))
    value2 = int(input("Enter the second Number"))
    ret = ChkGreate(value1,value2)
    if(ret == None):
        print("both are equal number")
    else:
        print("greater number is : ",ret)

if __name__ == "__main__":
    main()
def CheckPrime(No):
    if No <= 1:
        return False
    for i in range(2,int(No),1):
        if No%i==0:
            return False
    return True
     
def main():
    value1 = int(input("Enter the Number"))
    ret = CheckPrime(value1)
    if ret == True:
        print("Yes, it is Prime")
    else:
        print("NO. it is not Prime")
    
if __name__ == "__main__":
    main()
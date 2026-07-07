def CheckDivisible(No1):
    if No1%5 == 0:
        return True
    else:
        return False
                    
def main():
    Value1 = int(input("inter First Number"))
    ret = CheckDivisible(Value1)
    if ret == True:
        print(ret)
    else:
        print(ret)
    

if __name__ == "__main__":
    main()

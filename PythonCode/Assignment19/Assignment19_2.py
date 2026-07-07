import sys
Power = lambda No1,No2 : (No1*No2)

def main():
    value1 = int(input("enter number"))
    value2 = int(input("enter number"))
    ret = Power(value1,value2)
    print(ret)

if __name__ == "__main__":
    main()
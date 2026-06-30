
def AreaOfRectAngle(No1,No2):
    return No1*No2
    
def main():
    value1 = int(input("enter length of reactangle : "))
    value2 = int(input("enter width of reactangle : "))
    ret = AreaOfRectAngle(value1,value2)
    print("Area of ract angle is : ", ret)
    
if __name__ == "__main__":
    main()


def AreaOfCircle(No1):
    return 3.14*(No1*No1)
    
def main():
    value1 = int(input("enter radious of circle : "))
    ret = AreaOfCircle(value1)
    print("Area of circle is : ", ret)
    
if __name__ == "__main__":
    main()

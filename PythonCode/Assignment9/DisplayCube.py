def Cube(No):
    return No * No * No
    
    
def main():
    value1 = int(input("Enter the Number"))
    ret = Cube(value1)
    print("cube is : ",ret)

if __name__ == "__main__":
    main()
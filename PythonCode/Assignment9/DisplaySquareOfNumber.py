def Square(No):
    return No * No
    
    
def main():
    value1 = int(input("Enter the Number"))
    ret = Square(value1)
    print("Square is : ",ret)

if __name__ == "__main__":
    main()
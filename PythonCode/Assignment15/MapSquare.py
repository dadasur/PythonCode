Square = lambda No : (No*No)    
    
def main():
    Values = list(map(int,input("Enter the Number in list").split()))
    ret = list(map(Square,Values))
    print("Square is : ",ret)

if __name__ == "__main__":
    main()
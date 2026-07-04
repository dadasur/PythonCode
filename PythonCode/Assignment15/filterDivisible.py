Divisible = lambda No: (No%3==0 and No%5==0)
    
    
def main():
    Values = list(map(int,input("Enter the Number in list").split()))
    ret = list(filter(Divisible,Values))
    print(ret)

if __name__ == "__main__":
    main()
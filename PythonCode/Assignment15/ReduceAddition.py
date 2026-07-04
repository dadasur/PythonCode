from functools import reduce
Addition = lambda No1,No2 : No1+No2
        
def main():
    Values = list(map(int,input("Enter the Number in list").split()))
    ret = reduce(Addition,Values)
    print(ret)

if __name__ == "__main__":
    main()
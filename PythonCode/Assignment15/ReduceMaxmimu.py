from functools import reduce

ChkGreate = lambda No1,No2 : No1 if (No1 > No2) else No2
            
def main():
    Values = list(map(int,input("Enter the Number in list").split()))
    ret = reduce(ChkGreate,Values)
    print(ret)

if __name__ == "__main__":
    main()
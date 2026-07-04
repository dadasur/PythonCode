from functools import reduce

ChkMinimum = lambda No1,No2 : No1 if (No1 < No2) else No2
            
def main():
    Values = list(map(int,input("Enter the Number in list").split()))
    ret = reduce(ChkMinimum,Values)
    print(ret)

if __name__ == "__main__":
    main()
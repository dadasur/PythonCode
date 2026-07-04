ChkMiniMum = lambda No1,No2 : No1 if (No1 < No2) else No2
            
def main():
    value1 = int(input("Enter the first Number"))
    value2 = int(input("Enter the second Number"))
    ret = ChkMiniMum(value1,value2)
    print("minimum number is ",ret)

if __name__ == "__main__":
    main()
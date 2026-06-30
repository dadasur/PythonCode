def SumOfN(No):
    return int(No*(No+1)/2)
    
    
def main():
    value1 = int(input("Enter the Number"))
    ret = SumOfN(value1)
    print(ret)

if __name__ == "__main__":
    main()
CheckEven=lambda No : No%2==0
        
def main():
    Values = list(map(int,input("Enter the Number in list").split()))
    ret = list(filter(CheckEven,ValueError))
    print(ret)

if __name__ == "__main__":
    main()
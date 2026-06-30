def Divisible(No):
    return No%3
    
    
def main():
    value1 = int(input("Enter the Number"))
    ret = Divisible(value1)
    if ret == 0:
        print("Yes, it is divisible by 3")
    else:
        print("No, it is not divisible by 3")

if __name__ == "__main__":
    main()
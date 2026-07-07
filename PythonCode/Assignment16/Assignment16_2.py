def CheckEvenOdd(No):
    if No%2==0:
        return "even number"
    else:
        return "Odd number"

def main():
    Value1 = int(input("inter Number"))
    ret = CheckEvenOdd(Value1)
    print(ret)

if __name__ == "__main__":
    main()

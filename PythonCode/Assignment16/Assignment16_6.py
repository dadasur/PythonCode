def CheckPositiveNigative(No1):
    if No1 <= -1 :
        return "Number is nigative"
    elif No1 > 0:
        return "Number is positive"
    else:
        return "Numbe is zero"
        
            
def main():
    Value1 = int(input("inter First Number"))
    ret = CheckPositiveNigative(Value1)
    print(ret)
    

if __name__ == "__main__":
    main()

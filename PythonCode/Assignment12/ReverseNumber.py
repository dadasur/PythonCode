
def ReverseNumber(No):
    res = []
    while No > 0:
         res.append(No)
         No = No - 1        
    return(res)
    
    

def main():
    value = int(input("enter one number : "))
    ret = ReverseNumber(value)
    print(ret)
    
if __name__ == "__main__":
    main()

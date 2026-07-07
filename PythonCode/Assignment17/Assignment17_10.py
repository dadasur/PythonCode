def Digit(No):
    sum = 0
    while int(No) > 0:
        digit = int(No)%10
        sum = sum + digit       
        No = int(No)/10
    return sum
    

   
def main():
    value = int(input("Enter value"))
    ret = Digit(value)
    print("Addition  is",ret)

if __name__ == "__main__":
    main()
       





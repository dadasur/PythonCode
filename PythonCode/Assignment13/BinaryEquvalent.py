
def BinaryEquvalent(No1):

    binarystr = ""
    reverse = 0
    count = 0

    while int(No1) > 0:
       reminder = int(No1) % 2
       No1 = int(No1) / 2
       binarystr = binarystr+str(reminder)
    
    count = len(binarystr)
    while count !=0:
        digit = int(binarystr)%10
        reverse = reverse * 10 + digit
        binarystr = int(binarystr) / 10
        count = count-1
    return reverse
        
def main():
    value1 = int(input("enter Number : "))
    ret = BinaryEquvalent(value1)
    print("binary of "+str(value1)+" is: ",ret)
    
if __name__ == "__main__":
    main()

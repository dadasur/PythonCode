def Digit(No):
    count = 0
    while int(No) > 0:       
        No = int(No)/10
        count = count + 1
    return count
    

   
def main():
    value = int(input("Enter value"))
    ret = Digit(value)
    print("length is",ret)

if __name__ == "__main__":
    main()
       





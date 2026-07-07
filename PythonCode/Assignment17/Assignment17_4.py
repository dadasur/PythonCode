def factoreal(No):
    fact = 0
    for i in range(1,No):
        if No%i==0:
            fact = fact + i
    return fact

   
def main():
    value = int(input("Enter value"))
    ret = factoreal(value)
    print("factorieal is",ret)

if __name__ == "__main__":
    main()
       





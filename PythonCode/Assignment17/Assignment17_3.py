def factoreal(No):
    fact = 1
    for i in range(1,No+1):
        fact = fact * i
    return fact

   
def main():
    value = int(input("Enter value"))
    ret = factoreal(value)
    print("factorieal is",ret)

if __name__ == "__main__":
    main()
       





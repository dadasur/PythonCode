def checkprime(No):
     if No <= 1:
      return False       
     for i in range(2,int(No),1):
        if No%i==0:
            return False
     return True

def main():
    value = int(input("enter number "))
    ret = checkprime(value)
    if ret == True:
     print("it is prime number")
    else:
        print("it is not prime number")


if __name__ == "__main__":       
        main()

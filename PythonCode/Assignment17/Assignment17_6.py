def DisplayMatrics(No):
    No1 = No
    for i in range(No):        
        for j in range(No1):
            print("*", end=" ")
        No1 = No1 - 1
        print()

def main():
    value = int(input("Enter value"))
    DisplayMatrics(value)

if __name__ == "__main__":
    main()
       





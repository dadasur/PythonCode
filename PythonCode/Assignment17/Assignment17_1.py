import Arithmetic

def main():
        value1 = int(input("enter first number"))
        value2 = int(input("enter second number"))
        print("Addtion is", Arithmetic.Addition(value1,value2))
        print("Subtraction is", Arithmetic.Subtraction(value1,value2))
        print("Multiplecation", Arithmetic.Multiplecation(value1,value2))
        print("Division is", Arithmetic.Division(value1,value2))

if __name__ == "__main__":
        
        main()
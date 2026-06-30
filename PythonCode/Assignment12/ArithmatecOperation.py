
def ArithmatecOperation(No1,No2):
    Result = []
    Result.append(No1+No2)
    Result.append(No1-No2)
    Result.append(No1*No2)
    Result.append(No1/No2)
    return Result
    

def main():
    value1 = int(input("enter first number : "))
    value2 = int(input("enter second number : "))
    ret = ArithmatecOperation(value1,value2)
    print("Addition is", ret[0])
    print("subtarction is", ret[1])
    print("multiplication is", ret[2])
    print("devision is", ret[3])
    
if __name__ == "__main__":
    main()

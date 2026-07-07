import sys

def search(Data,Value):
    count = 0 
    for i in Data:
        if i == Value:
            count = count + 1
    return count

def main():
     n = input("Enter All N Number sepreated by space : ")
     values = []
     for i in n.split():
            values.append(int(i))
    
     No = int(input("enter search element")) 
     ret = search(values,No)
     print("frequency of Element is",ret)



if __name__ == "__main__":
    main()
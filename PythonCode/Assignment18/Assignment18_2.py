import sys

def Max(Data):
    max = Data[0] 
    for i in Data:
        if i > max:
            max = i
    return max

def main():
     n = input("Enter All N Number sepreated by space : ")
     values = []
     for i in n.split():
            values.append(int(i))
     ret = Max(values)
     print("Max Element is",ret)



if __name__ == "__main__":
    main()
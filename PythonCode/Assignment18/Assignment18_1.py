import sys

def Addition(Data):
    sum = 0 
    for i in Data:
        sum = sum + i
    return sum

def main():
     n = input("Enter All N Number sepreated by space : ")
     values = []
     for i in n.split():
            values.append(int(i))
     ret = Addition(values)
     print(ret)

if __name__ == "__main__":
    main()
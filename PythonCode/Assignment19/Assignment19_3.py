from functools import reduce

def CheckNumber(no):
    if no >= 70 and no<=90:
        return no
def Increment(no):
    no = no + 10
    return no

Product = lambda No1,No2 : No1*No2

def main():
    n = input("Enter All N Number sepreated by space : ")

    values = []
    for i in n.split():
        values.append(int(i))
    print(values)

    fret = list(filter(CheckNumber,values))
    print(fret)
    mret = list(map(Increment,fret))
    print(mret)
    rret = reduce(Product,mret)
    print(rret)



if __name__ == "__main__":
    main()
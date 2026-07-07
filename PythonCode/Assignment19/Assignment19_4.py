from functools import reduce

def CheckEven(no):
    if no%2==0:
        return no
    
def squeare(no):
    return no*no

Addition = lambda No1,No2 : No1+No2

def main():
    n = input("Enter All N Number sepreated by space : ")

    values = []
    for i in n.split():
        values.append(int(i))
    print(values)

    fret = list(filter(CheckEven,values))
    print(fret)
    mret = list(map(squeare,fret))
    print(mret)
    rret = reduce(Addition,mret)
    print(rret)



if __name__ == "__main__":
    main()
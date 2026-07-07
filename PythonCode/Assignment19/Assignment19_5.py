 
from functools import reduce

def CheckPrime(No):
    if No <= 1:
        return False
    for i in range(2,int(No),1):
        if No%i==0:
            return False
    return True


def Fnumbers(no):
     
        if CheckPrime(no):
            return no

def Incriment(no):
    return no*2

def Max(no1,no2):
    if no1 > no2:
        return no1
    else:
        return no2
    
def main():
    n = input("Enter All N Number sepreated by space : ")

    values = []
    for i in n.split():
        values.append(int(i))

    fret = list(filter(Fnumbers,values))
    print(fret)
    mret = list(map(Incriment,fret))
    print(mret)
    rret = reduce(Max,mret)
    print(rret)



if __name__ == "__main__":
    main()
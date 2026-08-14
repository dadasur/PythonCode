#UDKNN1.py
import math
import numpy as np
def MarvellousEucDistance(P1,P2):
    Ans = math.sqrt((P1['X']-P1['Y'])**2 + (P2['X']-P2['Y'])**2)
    return Ans
def MarvellousKNNcalissifier(X,Y,K = 3):
    border = "-"*30
    Data = [
        {'point' : 'A', 'X' : 1,'Y':2,'label':'Red'},
        {'point' : 'B', 'X' : 2,'Y':3,'label':'Red'},
        {'point' : 'C', 'X' : 3,'Y':1,'label':'Blue'},
        {'point' : 'D', 'X' : 6,'Y':5,'label':'Blue'},
        {'point' : 'E', 'X' : 6,'Y':6,'label':'Blue'},
        {'point' : 'F', 'X' : 3,'Y':4,'label':'Red'},
        {'point' : 'G', 'X' : 3,'Y':2,'label':'Red'}
    ]
    print(border)
    print("Marvellous classifier")
    print(border)

    for i in Data:
        print(i)
    print(border)

    new_point = {'X' : X,'Y' : Y}

    print("Distance of all points")
    print(border)

    for d in Data:

        d['Distance'] = MarvellousEucDistance(d,new_point)

    for d in Data:
        print(d)
    print(border)
    
    sorted_data = sorted(Data,key=lambda item : item['Distance'])
    print(border)
    print("sorted data :")
    print(border)

    nearest = sorted_data[:K]
    
    print(border)
    #voting
    
    votes = {}

    for neifbours in nearest:
        lable = neifbours['label']
        votes[lable] = votes.get(lable,0) + 1
    print(border)
    print("voting result is ")

    for d in votes:
        print("name : ",d,"numbe of vote : ", votes[d])

    iMax = 0
    Name = ""
    for d in votes:
        if(votes[d] > iMax):
            iMax = votes[d]
            Name = d
    print("final predication is : ",Name)

def main():
    x = int(input("Enter the value for X: "))
    y = int(input("Enter the value for Y: "))
    
    for i in range(1,6,2):

     MarvellousKNNcalissifier(x,y,i)
     print("hyper tuning parameter is : ",i)


if __name__ ==  "__main__":
    main()
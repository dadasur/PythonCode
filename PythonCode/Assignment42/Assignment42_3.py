#UDKNN1.py
import math
import numpy as np
def StudentEucDistance(P1,P2):
    Ans = math.sqrt((P1['Study Hours']-P1['Attendance'])**2 + (P2['Study Hours']-P2['Attendance'])**2)
    return Ans
def Studentcalissifier(X,Y,K = 5):
    border = "-"*30
    Data = [
        {'point' : 'A', 'Study Hours' : 2,'Attendance':60,'Result':'Fail'},
        {'point' : 'B', 'Study Hours' : 5,'Attendance':80,'Result':'Pass'},
        {'point' : 'C', 'Study Hours' : 6,'Attendance':85,'Result':'Pass'},
        {'point' : 'D', 'Study Hours' : 1,'Attendance':50,'Result':'Fail'},
        
    ]
    print(border)
    print("Marvellous classifier")
    print(border)

    for i in Data:
        print(i)
    print(border)

    new_point = {'Study Hours' : X,'Attendance' : Y}

    print("Distance of all points")
    print(border)

    for d in Data:

        d['Distance'] = StudentEucDistance(d,new_point)

    for d in Data:
        print(d)
    print(border)
    sorted_data = sorted(Data,key=lambda item : item['Distance'])
    print(border)
    print("sorted data :")
    print(border)
    
    for d in sorted_data:
        print(d)
    print(border)

    nearest = sorted_data[:K]
        
    print(border)
    
    for d in nearest:
        print(d)
    
    print(border)
        #voting
    votes = {}
    
    for neifbours in nearest:
        lable = neifbours['Result']
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
        print("final prediction is : ",Name)
    
def main():
    x = int(input("Enter the Study Hours: "))
    y = int(input("Enter the Attendance: "))
    
    Studentcalissifier(x,y,3)



if __name__ ==  "__main__":
    main()
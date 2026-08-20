#Linearregrsatiousrdefine1.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def MarvellusPredicater():
    #loda the data
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]
    print("values of independant varibale X :",X)
    print("values of dependant varibale Y :",Y)
    sum_x = 0
    sum_Y = 0
    for i in range(len(X)):
        sum_x = sum_x + X[i]
        sum_Y = sum_Y + Y[i]

    mean_X = sum_x/len(X)
    mean_Y = sum_Y/len(Y)
    print("mean_x is ",mean_X)
    print("mean_y is ",mean_Y)
    n = len(X) #5
    numrator = 0
    demorateor = 0
    # m= sum(x-xbar)*sum(Y-Ybar)/sum(x-xbar)**2
    for i in range(n):
        #calculate slope m
        numrator = numrator +((X[i]-mean_X)*(Y[i]-mean_Y))
        demorateor = demorateor + ((X[i]-mean_X)**2)
    m = numrator/demorateor
    print("slop line m :",m)
    #y= mx+c
    #c = ymean-m*xmean
    c = mean_Y - m  * mean_X
    print("Yintercept ie C:",c)
    x = np.linspace(1,6,n)
    y = c + m * x

    #predicated value of yp
    predicated = []
    for i in range(len(X)):
        predicated.append(0.4*X[i]+2.4)
    for i in range(len(X)):
        print(predicated[i])
    #residesalmvalue
    residesal = []
    for i in range(len(X)):
        residesal.append(Y[i]-predicated[i])
    for i in residesal:
        print(round(i,6))
    #Mean Squared Error (MSE)
    MSE = mean_Y /len(X)
    print("MSE is ",MSE)
    #R-Squared (R)**2
    #Y-Yp**2
    sumyp =0
    for i in residesal:
        sumyp = sumyp + i**2
    print("Y-Yp2 = ",round(sumyp,6))

    #Y-Ymen**2
    sumy =0 
    for i in range(len(Y)):
        sumy = sumy + (Y[i]-mean_Y)**2
    print("y-ymean saw",round(sumy,6))

    #calculate R2
    R = 1 - (sumyp/5.2)
    print("model explain only",round(R,6)) 

    plt.plot(x,y,color = 'g',label = "Regration Line")
    plt.scatter(X,Y,color = 'r',label = "Sacter a plot")
    plt.xlabel("X:independant varbles")
    plt.ylabel("Y : dependat varible")
    plt.legend()
    plt.show()

def main():
    MarvellusPredicater()

if __name__ == "__main__":
    main()
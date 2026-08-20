#Linearregrsatiousrdefine1.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def MarvellusPredicater():
    #loda the data
    X = [1,2,3,4,5]
    Y = [20000,25000,30000,35000,40000]
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
    predicated = m*6+c
    print("predited result is ",predicated)

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
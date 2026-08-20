#Linearregrationadvestrting1.py
#Advertising
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score

def MarvellosRegration(Datapatha):
    #step 1 : load the data
    Border = "-"*40
    print(Border)
    print("load in data")
    print(Border)
    df = pd.read_csv(Datapatha)
    print(df.head())
    #step 2 : eremove unwanted colunm
    print(Border)
    print("eremove unwanted colunm")
    print(Border)
    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])
    print(df.head())

    #setp 3 check missing values
    print(Border)
    print("check missing valuse")
    print(Border)
    print("taoatal misii valyes") #canolical
    print(Border)
    print(df.isnull().sum())
    print(Border)
    #step 4 statical summary
    print(Border)
    print("step 4 statical summary")
    print(Border)
    print(df.describe())

    # tep 5 coleration
    print(Border)
    print("step 5 coleration")
    print(Border)
    print(df.corr())

    #setp 6 seprate independant ande depandnt varibles
    print(Border)
    print("step 6 split independant ande depandnt varibles")
    print(Border)

    X = df[["TV","radio","newspaper"]] 

    Y =df["sales"]
    print("indpedant varible")
    print(X.head())
    print("dep varible")
    print(Y.head())

    #step 7 split the data set
    print(Border)
    print("step 7 split the data set")
    print(Border)

    X_train,X_test,Y_train,Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
    )
    print("Traning data",X_train.shape)
    print("testing data",X_test.shape)

    #step * cretae and train the model

    print(Border)
    print("step 8 cretae and train the model")
    print(Border)

    model = LinearRegression()
    model = model.fit(X_train,Y_train)
    print("model tarined successfully.....")

    #step 9 test the maodel
    print(Border)
    print("step 9 test the maodel")
    print(Border)

    Y_pred = model.predict(X_test)
    print("expecte anser")
    print(Y_test[:10])

    print("predicted anser")
    print(Y_pred[:10])

    #10 evelute the model
    print(Border)
    print("10 evelute the model")
    print(Border)

    MSE = mean_squared_error(Y_test,Y_pred)
    RMSE = np.sqrt(MSE)
    R2 = r2_score(Y_test,Y_pred)
    print("MSE: ",MSE)
    print("RMSE: ",RMSE)
    print("Rsquere: ",R2)


    #step 11 display quefetion 
    print(Border)
    print("step 11 display quefetion ")
    print(Border)
    print("Tv coeff:",model.coef_[0])
    print("radio coeff:",model.coef_[1])
    print("newspaper coeff:",model.coef_[2])

    print("intersect",model.intercept_)

    

def main():
    MarvellosRegration("Advertising.csv")

if __name__ == "__main__":
    main()
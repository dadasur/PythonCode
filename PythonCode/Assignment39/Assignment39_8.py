#casestudystep2.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (accuracy_score,confusion_matrix,classification_report)
Border = "-"*30
##########################################################
#step 1 load the data set
##########################################################

print(Border)
print("step 1 : load the dataset")
print(Border)

datapath = "student_performance_ml.csv"
#df = pd.read_excel(datapath)
df = pd.read_csv(datapath)
print("data set loded sucessfully ")
print("inital entry from datas et are ")
print(df.head())

##########################################################
#step 2 Data analysys (EDA)Explontry
##########################################################

print(Border)
print("step 2 Data analysys (EDA)Explontry")
print(Border)
print("shape of data set",df.shape)
print("clunm name : ",list(df.columns))
print("missing values per colunm : ")
print(df.isnull().sum())#canlicak function
print("class distrubution(spices count)")
print(df["FinalResult"].value_counts())
print("static cal trpot of dataset ")
print(df.describe())

##########################################################
#step 3 deside indepedand dependant varibles
##########################################################
print(Border)
print("step 3 deside indepedand dependant varibles")
print(Border)

#x : indepedant varible / frtures
#Y : depedant varible / labels

feture_cols = ["StudyHours","Attendance","PreviousScore","SleepHours"]
X = df[feture_cols]
Y = df["FinalResult"]

print("X shape : ",X.shape)
print("Y shape : ",Y.shape)

##########################################################
#step 4 visulization of dataset
##########################################################
print(Border)
print("step 4 visulization of dataset")
print(Border)

plt.figure(figsize=(7,5))

for sp in df["FinalResult"].unique():
    temp = df[df["FinalResult"]== sp]
    plt.scatter(temp["StudyHours"], temp["Attendance"],label=sp)

plt.title("Marvelloi irs case studu")
plt.xlabel("StudyHours")
plt.ylabel("Attendance")
plt.legend()
plt.grid()
plt.show()

##########################################################
#step 5 split the dataset for tarning and testing
##########################################################
print(Border)
print("step 5 split the dataset for tarning and testing")
print(Border)

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)
print("data set split activet done")

print("X_tarin : ",X.shape)
print("x_tarin : ",Y.shape) 

print("X_tarin : ",X_train.shape)
print("x_tarin : ",X_test.shape)

print("X_tarin : ",Y_train.shape) 
print("x_tarin : ",Y_test.shape)

##########################################################
#step 6 Build the model
##########################################################
print(Border)
print("step 6 Build the model")
print(Border)

model = DecisionTreeClassifier(max_depth=6)

print("model get cretaed sucess fully")

##########################################################
#step 7 Traind the model
##########################################################
print(Border)
print("step 7 Traind the model")
print(Border)

model.fit(X_train,Y_train)

print("model tarend sucess fully")

##########################################################
#step 8 test the model
##########################################################
print(Border)
print("step 8 test the model")
print(Border)

Y_pred = model.predict(X_test)

print("model testing done")

print("Expected ansers : ")
print(Y_test)
print(Y_pred)



##########################################################
#step 9 evalute the module performance
##########################################################
print(Border)
print("step 9 evalute the module performance")
print(Border)

accurecy = accuracy_score(Y_test,Y_pred)
print("accurcy of model is ", accurecy*100)
print("cnfustion matrix")
cm = confusion_matrix(Y_test,Y_pred)
print(cm)
print("classification report")
print(classification_report(Y_test,Y_pred))


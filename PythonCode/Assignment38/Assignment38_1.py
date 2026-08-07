#casestudystep2.py
import pandas as pd
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
print(df.tail())
print("Total rows:", df.shape[0])
print("Total columns:", df.shape[1])
print("Column names:")
print(list(df.columns))

print("Data type of each column:")
print(df.dtypes)








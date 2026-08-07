
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
print("Number of students in the data set:", df.shape[0])
print(df["FinalResult"].value_counts())
pass_count = (df["FinalResult"] == 0).sum()
fail_count = (df["FinalResult"] == 1).sum()
print("Number of students passed:", pass_count)
print("Number of students failed:", fail_count)
















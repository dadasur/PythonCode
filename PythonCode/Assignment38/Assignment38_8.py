import pandas as pd
import matplotlib.pyplot as plt

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
##########################################################
#step 4 visulization of dataset
##########################################################
plt.figure(figsize=(6, 4))

plt.boxplot(df["Attendance"])

plt.title("Boxplot of Attendance")
plt.ylabel("Attendance")

plt.show()
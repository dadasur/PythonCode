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
pass_rate = df.groupby("AssignmentsCompleted")["FinalResult"].mean() * 100

plt.figure(figsize=(7, 4))
plt.bar(pass_rate.index.astype(str), pass_rate.values)
plt.title("Pass Rate by Assignments Completed")
plt.xlabel("Assignments Completed")
plt.ylabel("Pass Rate (%)")
plt.ylim(0, 110)
plt.grid(axis="y", linestyle="--", alpha=0.4)
plt.show()

print("Pass rate by assignments (%):")
print(pass_rate.round(1))
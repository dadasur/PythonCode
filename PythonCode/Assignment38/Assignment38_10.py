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
plt.figure(figsize=(7, 4))
plt.scatter(df["SleepHours"], df["FinalResult"], alpha=0.7)

plt.title("SleepHours vs FinalResult")
plt.xlabel("SleepHours")
plt.ylabel("FinalResult")
plt.yticks([0, 1], ["Fail", "Pass"])

plt.show()
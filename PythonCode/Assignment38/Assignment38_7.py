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
plt.figure(figsize=(7,5))

for sp in df["FinalResult"].unique():
    temp = df[df["FinalResult"]== sp]
    plt.scatter(temp["StudyHours"], temp["PreviousScore"],label=sp)

plt.title("StudyHours vs PreviousScore with Trendline")
plt.xlabel("StudyHours")
plt.ylabel("PreviousScore")
plt.legend()
plt.grid()
plt.show()

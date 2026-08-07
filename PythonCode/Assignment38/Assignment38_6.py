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
plt.hist(df["StudyHours"], bins=8, edgecolor="black")

plt.title("Distribution of Study Hours")
plt.xlabel("Study Hours")
plt.ylabel("Number of Students")

plt.show()
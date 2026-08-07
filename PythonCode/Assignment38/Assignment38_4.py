
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

counts = df["FinalResult"].value_counts()
percentages = df["FinalResult"].value_counts(normalize=True) * 100

print("Pass students:", counts[1])
print("Fail students:", counts[0])

print("Pass percentage: {:.2f}%".format(percentages[1]))
print("Fail percentage: {:.2f}%".format(percentages[0]))

print("Justification : " \
"balanced dataset usually has almost equal number of samples in each class." \
"but in our case " \
"Pass = 18" \
"Fail = 12" \
"This gives a 60:40 distribution, which shows one class is more common than the other." \
"The dataset is slightly imbalanced")















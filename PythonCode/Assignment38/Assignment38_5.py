
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

print("Based on this dataset, higher StudyHours clearly increases the chance of passing. Students with study hours below about 4 mostly failed, while students with 4.2 or more hours consistently passed." \
"A similar pattern appears for Attendance. Students with attendance up to around 75% mostly failed, while those with 76% or higher mostly passed." \
"So, both StudyHours and Attendance show a strong positive relationship with FinalResult in this dataset." \
"This suggests that students who study more and attend classes regularly have a better chance of passing")





#9011893700









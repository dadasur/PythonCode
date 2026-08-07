
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
avg_study_hours = df["StudyHours"].mean()
avg_attendance = df["Attendance"].mean()
max_prev_score = df["PreviousScore"].max()
min_sleep_hours = df["SleepHours"].min()

print(f"Average StudyHours: {avg_study_hours:.2f}")
print(f"Average Attendance: {avg_attendance:.2f}")
print(f"Maximum PreviousScore: {max_prev_score}")
print(f"Minimum SleepHours: {min_sleep_hours}")
















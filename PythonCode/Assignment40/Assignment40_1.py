#casestudystep2.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (accuracy_score,confusion_matrix,classification_report)
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
##########################################################
# Build the model
##########################################################
X = df[[
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
]]

y = df["FinalResult"]

# Train model
model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X, y)


feature_importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance Score": model.feature_importances_
})

feature_importance = feature_importance.sort_values(
    by="Importance Score",
    ascending=False
)

print("Feature Importance Scores:")
print(feature_importance)

print("\nMost important feature:", feature_importance.iloc[0]["Feature"])
print("Least important feature:", feature_importance.iloc[-1]["Feature"])







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
    "AssignmentsCompleted"
]]

# Target feature
y = df["FinalResult"]

# Split dataset into train and test data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create and train the Decision Tree model
model = DecisionTreeClassifier(max_depth=5, random_state=42)
model.fit(X_train, y_train)

# Predict test results
y_pred = model.predict(X_test)

# Calculate new testing accuracy
new_accuracy = accuracy_score(y_test, y_pred)

print(f"New Testing Accuracy: {new_accuracy * 100:.2f}%")

previous_accuracy = 100.0

print(f"Previous Accuracy with SleepHours: {previous_accuracy:.2f}%")
print(f"New Accuracy without SleepHours: {new_accuracy * 100:.2f}%")

if new_accuracy * 100 == previous_accuracy:
    print("Removing SleepHours did not affect model performance.")
elif new_accuracy * 100 < previous_accuracy:
    print("Removing SleepHours reduced model performance.")
else:
    print("Removing SleepHours improved model performance.")



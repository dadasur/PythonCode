#casestudystep2.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (accuracy_score,confusion_matrix,classification_report,ConfusionMatrixDisplay)
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
X = df[["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted"]]
y = df["FinalResult"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

print("Model trained successfully")


y_pred = model.predict(X_test)

# Manual accuracy calculation
correct_predictions = (y_pred == y_test.values).sum()
total_predictions = len(y_test)

manual_accuracy = correct_predictions / total_predictions

print(f"Correct predictions: {correct_predictions}")
print(f"Total predictions: {total_predictions}")
print(f"Manual Accuracy: {manual_accuracy * 100:.2f}%")

# Verify with sklearn
sklearn_accuracy = accuracy_score(y_test, y_pred)

print(f"Scikit-learn Accuracy: {sklearn_accuracy * 100:.2f}%")

# Check whether both match
if manual_accuracy == sklearn_accuracy:
    print("Verification successful: Manual accuracy matches scikit-learn accuracy.")
else:
    print("The accuracy values do not match.")
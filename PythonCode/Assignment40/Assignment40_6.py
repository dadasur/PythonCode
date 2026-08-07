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
X = df[[
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
]]

y = df["FinalResult"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)

# Create and train the model
reduced_model = DecisionTreeClassifier(max_depth=3, random_state=42)
reduced_model.fit(X_train, y_train)

# Predict test results
y_pred = reduced_model.predict(X_test)

# Combine feature values with actual and predicted results
comparison = X_test.copy()
comparison["ActualResult"] = y_test.values
comparison["PredictedResult"] = y_pred

# Add readable result labels
comparison["ActualLabel"] = comparison["ActualResult"].map({
    0: "Fail",
    1: "Pass"
})

comparison["PredictedLabel"] = comparison["PredictedResult"].map({
    0: "Fail",
    1: "Pass"
})

# Show only incorrect predictions
misclassified = comparison[
    comparison["ActualResult"] != comparison["PredictedResult"]
]

print("\nMisclassified Students:")
print(misclassified)

print("\nNumber of misclassified students:", len(misclassified))
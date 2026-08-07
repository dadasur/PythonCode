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

X = df[["StudyHours", "Attendance"]]

# Select target column
y = df["FinalResult"]

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Create and train the reduced model
reduced_model = DecisionTreeClassifier(max_depth=3, random_state=42)
reduced_model.fit(X_train, y_train)

# Create details for five new students
new_students = pd.DataFrame({
    "StudyHours": [2.5, 4.0, 5.5, 7.0, 3.0],
    "Attendance": [68, 75, 82, 90, 70]
})

# Predict results
predictions = reduced_model.predict(new_students)

new_students["PredictedResult"] = predictions

new_students["Prediction"] = new_students["PredictedResult"].map({
    0: "Fail",
    1: "Pass"
})

# Display predictions
print("\nPredictions for New Students:")
print(new_students)
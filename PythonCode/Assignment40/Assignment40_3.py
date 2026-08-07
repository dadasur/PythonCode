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
df = pd.read_csv(datapath)

# Target column
y = df["FinalResult"]

# Full-feature model
X_full = df[
    [
        "StudyHours",
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted"
    ]
]

# Reduced-feature model
X_reduced = df[
    [
        "StudyHours",
        "Attendance"
    ]
]

# Use the same split for a fair comparison
X_full_train, X_full_test, y_train, y_test = train_test_split(
    X_full,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

X_reduced_train, X_reduced_test, _, _ = train_test_split(
    X_reduced,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Train full-feature model
full_model = DecisionTreeClassifier(max_depth=5, random_state=42)
full_model.fit(X_full_train, y_train)

# Train reduced-feature model
reduced_model = DecisionTreeClassifier(max_depth=3, random_state=42)
reduced_model.fit(X_reduced_train, y_train)

full_prediction = full_model.predict(X_full_test)
reduced_prediction = reduced_model.predict(X_reduced_test)

# Calculate testing accuracy
full_accuracy = accuracy_score(y_test, full_prediction)
reduced_accuracy = accuracy_score(y_test, reduced_prediction)

# Display results
print(f"Full-feature model accuracy: {full_accuracy * 100:.2f}%")
print(f"StudyHours and Attendance model accuracy: {reduced_accuracy * 100:.2f}%")


if reduced_accuracy == full_accuracy:
    print("The reduced-feature model has the same performance as the full-feature model.")
elif reduced_accuracy < full_accuracy:
    print("The reduced-feature model performs worse than the full-feature model.")
else:
    print("The reduced-feature model performs better than the full-feature model.")

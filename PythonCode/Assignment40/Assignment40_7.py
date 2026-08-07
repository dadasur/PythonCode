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

df = pd.read_csv(datapath)

# Features and target
X = df[[
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted"
]]

y = df["FinalResult"]

# Different random states to compare
random_states = [0, 10, 42]

for rs in random_states:
    
    # Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=rs,
        stratify=y
    )

    # Create and train the model
    model = DecisionTreeClassifier(max_depth=3, random_state=rs)
    model.fit(X_train, y_train)

    # Predict test results
    y_pred = model.predict(X_test)

    # Calculate testing accuracy
    test_accuracy = accuracy_score(y_test, y_pred)

    print(f"random_state = {rs}")
    print(f"Testing Accuracy: {test_accuracy * 100:.2f}%")
    print()
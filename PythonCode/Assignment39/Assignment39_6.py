#casestudystep2.py
import pandas as pd
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
X = df[["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted", "SleepHours"]]
y = df["FinalResult"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

models = {
    "max_depth=1": DecisionTreeClassifier(max_depth=1, random_state=42),
    "max_depth=3": DecisionTreeClassifier(max_depth=3, random_state=42),
    "max_depth=None": DecisionTreeClassifier(max_depth=None, random_state=42)
}

for name, model in models.items():
    model.fit(X_train, y_train)

    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)

    train_acc = accuracy_score(y_train, y_train_pred)
    test_acc = accuracy_score(y_test, y_test_pred)

    print(name)
    print("Training Accuracy:", round(train_acc * 100, 2), "%")
    print("Testing Accuracy:", round(test_acc * 100, 2), "%")
    print()
#casestudystep2.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
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

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

print("Model trained successfully")


y_pred = model.predict(X_test)

# Generate confusion matrix
cm = confusion_matrix(y_test, y_pred)

# Display confusion matrix
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Fail", "Pass"])
disp.plot(cmap="Blues")

plt.title("Confusion Matrix")
plt.show()
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load dataset
datapath = "student_performance_ml.csv"
df = pd.read_csv(datapath)

# Create the new feature
df["PerformanceIndex"] = (df["StudyHours"] * 2) + df["Attendance"]

# Target column
y = df["FinalResult"]

# Original features
X_original = df[[
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted"
]]

# Features including PerformanceIndex
X_new = df[[
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "PerformanceIndex"
]]

# Use the same random state so comparison is fair
X_original_train, X_original_test, y_train, y_test = train_test_split(
    X_original,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

X_new_train, X_new_test, _, _ = train_test_split(
    X_new,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Train original model
original_model = DecisionTreeClassifier(max_depth=3, random_state=42)
original_model.fit(X_original_train, y_train)

# Train model with PerformanceIndex
new_model = DecisionTreeClassifier(max_depth=3, random_state=42)
new_model.fit(X_new_train, y_train)

# Calculate testing accuracies
original_prediction = original_model.predict(X_original_test)
new_prediction = new_model.predict(X_new_test)

original_accuracy = accuracy_score(y_test, original_prediction)
new_accuracy = accuracy_score(y_test, new_prediction)

print(f"Original Model Accuracy: {original_accuracy * 100:.2f}%")
print(f"New Model Accuracy: {new_accuracy * 100:.2f}%")

if new_accuracy > original_accuracy:
    print("Accuracy improved after adding PerformanceIndex.")
elif new_accuracy < original_accuracy:
    print("Accuracy decreased after adding PerformanceIndex.")
else:
    print("Accuracy did not change after adding PerformanceIndex.")
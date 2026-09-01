import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import AdaBoostClassifier

from tabulate import tabulate

#---------------------------------------
# Step 1 : Load the dataset
#---------------------------------------

df = pd.read_csv("Fraudulent_Transaction_Detection.csv")

print("Shape of dataset : ", df.shape)
print("First few records : ")
print(df.head())

#---------------------------------------
# Step 2 : Separate features and labels
#---------------------------------------

X = df.drop("Fraud", axis=1)
Y = df["Fraud"]

print("X shape : ", X.shape)
print("Y shape : ", Y.shape)

#---------------------------------------
# Step 3 : Split dataset for training and testing
#---------------------------------------

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

#---------------------------------------
# Step 4 : Scale the features
#---------------------------------------

scalar = StandardScaler()
X_train = scalar.fit_transform(X_train)
X_test = scalar.transform(X_test)

#---------------------------------------
# Step 5 : Create Individual models and store results
#---------------------------------------

results = []

# Helper function to get all metrics
def evaluate_model(name, Y_test, Y_pred):
    acc = accuracy_score(Y_test, Y_pred)
    prec = precision_score(Y_test, Y_pred)
    rec = recall_score(Y_test, Y_pred)
    f1 = f1_score(Y_test, Y_pred)
    tn, fp, fn, tp = confusion_matrix(Y_test, Y_pred).ravel()
    return [name, acc, prec, rec, f1, tn, fp, fn, tp]

# DecisionTreeClassifier
model_DC = DecisionTreeClassifier(random_state=42)
model_DC.fit(X_train, Y_train)
Y_pred_DC = model_DC.predict(X_test)
results.append(evaluate_model("Decision Tree", Y_test, Y_pred_DC))

# RandomForestClassifier
model_rnd = RandomForestClassifier(n_estimators=10, random_state=42)
model_rnd.fit(X_train, Y_train)
Y_pred_rnd = model_rnd.predict(X_test)
results.append(evaluate_model("Random Forest", Y_test, Y_pred_rnd))

# Bagging
base_model = DecisionTreeClassifier(random_state=42)
modelbag = BaggingClassifier(estimator=base_model, n_estimators=10, random_state=42)
modelbag.fit(X_train, Y_train)
Y_pred_bag = modelbag.predict(X_test)
results.append(evaluate_model("Bagging", Y_test, Y_pred_bag))

# Hard Voting
modelh = VotingClassifier(
    estimators=[
        ('logistic', LogisticRegression(max_iter=1000)),
        ('decision_tree', DecisionTreeClassifier(random_state=42)),
        ('knn', KNeighborsClassifier(n_neighbors=5))
    ],
    voting='hard'
)
modelh.fit(X_train, Y_train)
Y_pred_h = modelh.predict(X_test)
results.append(evaluate_model("Hard Voting", Y_test, Y_pred_h))

# AdaBoost
modelad = AdaBoostClassifier(n_estimators=50, learning_rate=1.0, random_state=42)
modelad.fit(X_train, Y_train)
Y_pred_ad = modelad.predict(X_test)
results.append(evaluate_model("AdaBoost", Y_test, Y_pred_ad))

#---------------------------------------
# Print Results in Tabular Format
#---------------------------------------

print("\n")
print(tabulate(
    results,
    headers=["Model", "Accuracy", "Precision", "Recall", "F1 Score", "TN", "FP", "FN", "TP"],
    tablefmt="grid",
    floatfmt=".4f"
))
# FNN_Employee_Deep.py
# Deep Learning - Feedforward Neural Network Pipeline (Procedural)
#
# Steps:
# 1. Read the data from CSV
# 2. EDA
# 3. Preprocessing
# 4. Train test split
# 5. Feature scaling
# 6. FNN model training
# 7. Model evaluation
# 8. Graphical representation
# 9. Test on unseen data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# --------------------------------------------------------------
# Constants used across the pipeline
# --------------------------------------------------------------

FEATURES = ['Age', 'MonthlyIncome', 'YearsAtCompany', 'TotalWorkingYears',
            'DistanceFromHome', 'JobSatisfaction', 'WorkLifeBalance', 'OverTime',
            'NumCompaniesWorked', 'TrainingTimesLastYear']

TARGET = 'Attrition'
DATA_FILE = "Employee_Attrition.csv"


# --------------------------------------------------------------
# Step 1: Read the data from CSV
# --------------------------------------------------------------

def load_data(path):
    print("Step 1: Read the data from CSV")
    data = pd.read_csv(path)
    print(data)
    return data


# --------------------------------------------------------------
# Step 2: EDA
# --------------------------------------------------------------

def explore_data(data):
    print("Step 2: Data analysis")
    print("First five rows:")
    print(data.head())
    print("Column names:")
    print(data.columns)
    print("Shape of data set:")
    print(data.shape)
    print("Statistical summary:")
    print(data.describe())


# --------------------------------------------------------------
# Step 3: Preprocessing
# --------------------------------------------------------------

def preprocess_data(data):
    print("Step 3: Preprocessing")
    data = data.copy()
    data['OverTime'] = (data['OverTime'] == "Yes").astype(int)
    label = LabelEncoder()
    data['Attrition'] = label.fit_transform(data['Attrition'])
    print(data.head())
    return data


# --------------------------------------------------------------
# Step 4: Train test split
# --------------------------------------------------------------

def split_data(X, Y):
    print("Step 4: Train test split")
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.20, random_state=42,stratify=Y
    )
    print("Training input shape :", X_train.shape)
    print("Testing input shape  :", X_test.shape)
    print("Training output shape:", Y_train.shape)
    print("Testing output shape :", Y_test.shape)
    return X_train, X_test, Y_train, Y_test


# --------------------------------------------------------------
# Step 5: Feature scaling
# --------------------------------------------------------------

def scale_features(X_train, X_test):
    print("Step 5: Feature scaling")
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    # FIX: transform only - scaler must never be fitted on test data
    X_test_scaled = scaler.transform(X_test)
    print("Scaled training data (first 5 rows):")
    print(X_train_scaled[:5])
    return scaler, X_train_scaled, X_test_scaled


# --------------------------------------------------------------
# Step 6: FNN model training
# --------------------------------------------------------------

def train_model(X_train_scaled, Y_train):
    print("Step 6: Model training")
    model = MLPClassifier(
        hidden_layer_sizes=(8, 4),
        activation="relu",
        solver="adam",
        max_iter=1000,
        random_state=42
    )
    print(model)
    model.fit(X_train_scaled, Y_train)
    print("Model training completed")
    print("Iterations required:", model.n_iter_)
    return model


# --------------------------------------------------------------
# Step 7: Model evaluation
# --------------------------------------------------------------

def evaluate_model(model, X_train_scaled, Y_train, X_test_scaled, Y_test):
    print("Step 7: Model evaluation")

    training_prediction = model.predict(X_train_scaled)
    training_accuracy = accuracy_score(Y_train, training_prediction)

    testing_prediction = model.predict(X_test_scaled)
    testing_accuracy = accuracy_score(Y_test, testing_prediction)

    print("Training accuracy :", training_accuracy * 100)
    print("Testing accuracy  :", testing_accuracy * 100)

    cm = confusion_matrix(Y_test, testing_prediction)
    print("Confusion matrix:")
    print(cm)

    accurecy_gap = training_accuracy - testing_accuracy
    
    if training_accuracy >=0.90 and accurecy_gap >= 0.10:
        print("it's s overfitting ")
    elif training_accuracy < 0.70 and testing_accuracy < 0.70:
        print("it's s underfitting ")
    elif abs(accurecy_gap) < 0.10 and training_accuracy >= 0.70:
        print("perfrom well ")
    else:
        print("need to analysys ")



# --------------------------------------------------------------
# Step 8: Graphical representation
# --------------------------------------------------------------

def plot_loss_curve(model):
    print("Step 8: Graphical representation")
    plt.figure(figsize=(8, 5))
    plt.plot(model.loss_curve_)
    plt.xlabel("Iteration")
    plt.ylabel("Loss")
    plt.title("MLP Training Loss Curve")
    plt.grid(True)
    plt.show()


# --------------------------------------------------------------
# Step 9: Test on unseen data
# --------------------------------------------------------------

def predict_unseen_data(model, scaler, new_data):
     print("Step 9: Prediction on unseen data")

     new_scaled = scaler.transform(new_data)
     new_prediction = model.predict(new_scaled)
     new_probability = model.predict_proba(new_scaled)


    # Human-readable verdict per employee
     for i, pred in enumerate(new_prediction):
        if pred == 1:
            print(f"Employee {i + 1}: Attrition (likely to leave)")
        else:
            print(f"Employee {i + 1}: No Attrition (likely to stay)")


# --------------------------------------------------------------
# Main pipeline - coordinates all the procedures
# --------------------------------------------------------------

def main():
    # Step 1: Read data
    data = load_data(DATA_FILE)

    # Step 2: EDA
    explore_data(data)

    # Step 3: Preprocessing
    data = preprocess_data(data)

    # Separate independent and dependent variables
    X = data[FEATURES]
    Y = data[TARGET]

    # Step 4: Train test split
    X_train, X_test, Y_train, Y_test = split_data(X, Y)

    # Step 5: Feature scaling
    scaler, X_train_scaled, X_test_scaled = scale_features(X_train, X_test)

    # Step 6: Model training
    model = train_model(X_train_scaled, Y_train)

    # Step 7: Model evaluation
    evaluate_model(model, X_train_scaled, Y_train, X_test_scaled, Y_test)

    # Step 8: Graphical representation
    plot_loss_curve(model)

    # Step 9: Test on unseen data
    new_data = pd.DataFrame(
        [ [24, 52421, 6, 6, 32, 4, 2, 1, 3, 0],   # young, overtime, long commute
            [45, 48000, 15, 20, 5, 3, 3, 0, 4, 3],  # mid-career, stable, no overtime
            [28, 32000, 2, 3, 18, 2, 2, 1, 1, 2],   # young, low income, overtime
            [38, 75000, 10, 15, 8, 4, 4, 0, 2, 3],  # senior, high income, satisfied
            [52, 98000, 22, 25, 3, 4, 3, 0, 5, 2],  # veteran, very high income
            [26, 29000, 1, 2, 25, 1, 2, 1, 6, 1],],
        columns=FEATURES
    )
    predict_unseen_data(model, scaler, new_data)


if __name__ == "__main__":
    main()

#Your model performs better on data it was trained on than on unseen data — that's the classic signature of overfitting.
#However, a gap of ~5–6% is small and quite normal in practice.
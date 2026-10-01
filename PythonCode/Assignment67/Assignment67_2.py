import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler

# 1. Dataset Setup
# Features: [Applicant Income, Credit Score, Loan Amount, Existing EMI, Employment Status]
X = np.array([
    [25000, 600, 200000, 10000, 0],
    [40000, 700, 300000, 8000, 1],
    [60000, 750, 500000, 12000, 1],
    [20000, 550, 150000, 15000, 0],
    [80000, 800, 700000, 10000, 1],
    [35000, 650, 250000, 9000, 1],
    [18000, 500, 100000, 12000, 0],
    [90000, 850, 800000, 15000, 1],
    [30000, 580, 200000, 14000, 0],
    [70000, 780, 600000, 10000, 1]
], dtype=np.float32)

y = np.array([0, 1, 1, 0, 1, 1, 0, 1, 0, 1], dtype=np.float32)

# Task 1: Preprocess Categorical Values
# Note: Employment Status is already encoded as binary numerical values (0 = Not Stable, 1 = Stable).

# Task 2: Apply Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Task 3: Build and Train FNN Model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(16, activation='relu', input_shape=(X.shape[1],)),
    tf.keras.layers.Dense(8, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')  # Binary classification
])

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Train the model
history = model.fit(X_scaled, y, epochs=100, verbose=1)

# Task 4: Evaluate Model
loss, accuracy = model.evaluate(X_scaled, y, verbose=0)
print(f"Model Training Accuracy: {accuracy * 100:.2f}%\n")

# Task 5: Predict Approval for New Applicant
new_applicant = np.array([[55000, 720, 400000, 10000, 1]], dtype=np.float32)

# Scale new input using fitted scaler
new_applicant_scaled = scaler.transform(new_applicant)

# Predict probability and output outcome
probability = model.predict(new_applicant_scaled, verbose=0)[0][0]
prediction = 1 if probability >= 0.5 else 0

status = "Loan Approved" if prediction == 1 else "Loan Rejected"

print(f"Prediction Probability: {probability:.4f}")
print(f"Prediction: {status} (Output Class: {prediction})")
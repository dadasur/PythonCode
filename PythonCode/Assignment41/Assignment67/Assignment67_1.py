import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Set random seeds for reproducibility
np.random.seed(42)
tf.random.set_seed(42)

# -----------------------------------------------------------------------------
# Task 1: Load/Create Dataset
# -----------------------------------------------------------------------------
# Features: [Age, Monthly charges, Tenure, Number of complaints, Customer support calls]
X = np.array([
    [25, 500, 12, 1, 2],
    [30, 700, 24, 0, 1],
    [45, 1200, 6, 5, 8],
    [50, 1500, 5, 6, 10],
    [28, 600, 18, 1, 1],
    [35, 800, 30, 0, 0],
    [48, 1400, 4, 7, 9],
    [52, 1600, 3, 8, 12],
    [27, 550, 20, 0, 1],
    [42, 1300, 8, 4, 7]
])

y = np.array([0, 0, 1, 1, 0, 0, 1, 1, 0, 1])

# -----------------------------------------------------------------------------
# Task 2: Clean the Dataset
# -----------------------------------------------------------------------------
# Check for null or missing values
assert not np.isnan(X).any(), "Dataset contains NaN values."
assert X.shape[0] == y.shape[0], "Feature and target lengths must match."

# -----------------------------------------------------------------------------
# Task 3: Apply StandardScaler
# -----------------------------------------------------------------------------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# -----------------------------------------------------------------------------
# Task 4: Train Feedforward Neural Network (FNN) Model
# -----------------------------------------------------------------------------
print("adm shape ",X.shape[1])
model = Sequential([
    Dense(8, activation='relu', input_shape=(X.shape[1],)),
    Dense(4, activation='relu'),
    Dense(1, activation='sigmoid')  # Binary classification
])

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Train the model
model.fit(X_scaled, y, epochs=150, verbose=0)

# -----------------------------------------------------------------------------
# Task 5: Evaluate Accuracy
# -----------------------------------------------------------------------------
loss, accuracy = model.evaluate(X_scaled, y, verbose=0)
print(f"Training Accuracy: {accuracy * 100:.2f}%\n")

# -----------------------------------------------------------------------------
# Test Input Prediction
# -----------------------------------------------------------------------------
new_customer = np.array([[46, 1450, 5, 6, 9]])

# Scale the test sample using the fitted scaler
new_customer_scaled = scaler.transform(new_customer)

# Make prediction
probability = model.predict(new_customer_scaled, verbose=0)[0][0]
prediction = 1 if probability >= 0.5 else 0

# Output interpretation
if prediction == 1:
    print(f"Prediction: Customer may leave (Probability: {probability:.2f})")
else:
    print(f"Prediction: Customer will stay (Probability: {1 - probability:.2f})")
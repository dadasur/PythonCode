# Task 1: Inputs, Initial Weight, Bias, Target Output, and Learning Rate
x = 2.0           # Input value
w_old = 0.8       # Initial weight
bias = 0.1        # Bias
y_target = 1.0    # Desired/Target output
learning_rate = 0.1

# Task 2: Calculate prediction (using a simple linear model: y_pred = w * x + b)
y_pred = (x * w_old) + bias

# Task 3: Calculate error and loss (Mean Squared Error derivative gradient step)
# Loss = 0.5 * (y_pred - y_target)^2
error = y_pred - y_target

gradient = error * x

# Task 4: Update weight using gradient descent logic: w_new = w_old - (learning_rate * gradient)
w_new = w_old - (learning_rate * gradient)

# Also update bias using gradient descent: b_new = b_old - (learning_rate * error)
bias_new = bias - (learning_rate * error)

# Task 5: Display results
print(f"Input (x):            {x}")
print(f"Target Output (y):    {y_target}")
print(f"Initial Prediction:   {y_pred:.4f}")
print(f"Error (y_pred - y):   {error:.4f}")
print(f"Calculated Gradient:  {gradient:.4f}")
print("-" * 35)
print(f"Old Weight (w_old):   {w_old:.4f}")
print(f"Updated Weight (w_new): {w_new:.4f}")
print(f"Updated Bias:         {bias_new:.4f}")
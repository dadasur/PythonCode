import math

# Inputs and Parameters
x1, x2 = 2, 3
w1, w2 = 0.4, 0.6
bias = 0.5

# Step 1: Calculate weighted sum (z)
weighted_sum = (x1 * w1) + (x2 * w2) + bias

# Step 2: Apply sigmoid activation function σ(z) = 1 / (1 + e^(-z))
output = 1 / (1 + math.exp(-weighted_sum))

# Step 3: Display results
print(f"Weighted Sum (z): {weighted_sum:.4f}")
print(f"Sigmoid Output: {output:.4f}")
print("The output is close to 1 (approximately 0.9569 or 95.69%).The sigmoid function squeezes any input value into the range $(0, 1)$. Because the weighted sum $z = 3.1$ is significantly greater than $0$, the sigmoid function maps it high up on the curve, placing it near $1$.")
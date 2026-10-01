import numpy as np
import matplotlib.pyplot as plt

# Define activation functions
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

def tanh(x):
    return np.tanh(x)

# 1. Accept input values from -10 to 10
x = np.linspace(-10, 10)
print(x)
# Calculate outputs
y_sigmoid = sigmoid(x)
y_relu = relu(x)
y_tanh = tanh(x)

# 2. Plot all activation functions using Matplotlib
plt.figure(figsize=(10, 6))

plt.plot(x, y_sigmoid, label="Sigmoid", color="blue", linewidth=2)
plt.plot(x, y_tanh, label="Tanh", color="green", linewidth=2)
plt.plot(x, y_relu, label="ReLU", color="red", linewidth=2)

plt.title("Activation Functions Visualization", fontsize=14)
plt.xlabel("Input Value (x)", fontsize=12)
plt.ylabel("Output Value f(x)", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(fontsize=12)
plt.ylim(-1.5, 10.5)

plt.show()
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("sigmoid : Used primary in the output layer of binary classification models because it outputs values interpretable as probabilities. It suffers from the vanishing gradient problem for extreme inputs.\n")
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("tanh : Preferred over Sigmoid in hidden layers because its output is zero-centered, which helps optimize gradient updates during backpropagation\n")
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("relu : The default choice for hidden layers in deep neural networks. It is computationally efficient and avoids vanishing gradients for positive inputs, enabling much faster training.\n")
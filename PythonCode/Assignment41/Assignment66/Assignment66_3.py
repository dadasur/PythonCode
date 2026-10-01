import numpy as np

def mean_squared_error(y_actuall_reg, y_pred):
    """Calculates MSE for regression tasks."""
    return np.mean((y_actuall_reg - y_pred) ** 2)

def binary_cross_entropy(y_actuall_cls, y_pred):
    epsilon = 1e-15
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
    
    loss = -np.mean(y_actuall_cls * np.log(y_pred) + (1 - y_actuall_cls) * np.log(1 - y_pred))
    return loss

y_actuall_reg = np.array([2.5, 0.0, 2.1, 7.8])
y_pred_reg = np.array([3.0, -0.5, 2.0, 7.2])

y_actuall_cls = np.array([1, 0, 1, 0])
y_pred_cls = np.array([0.9, 0.1, 0.8, 0.3])


mse_loss = mean_squared_error(y_actuall_reg, y_pred_reg)
bce_loss = binary_cross_entropy(y_actuall_cls, y_pred_cls)

print(f"Mean Squared Error (MSE) Loss:        {mse_loss:.4f}")
print(f"Binary Cross Entropy (BCE) Loss:     {bce_loss:.4f}")
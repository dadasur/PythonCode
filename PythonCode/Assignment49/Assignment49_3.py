import numpy as np
from sklearn.preprocessing import StandardScaler

def main():
    data = np.array([
    [25, 20000],
    [30, 40000],
    [35, 80000]
])
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    print("Scaled data:")
    print(scaled_data)

if __name__ == "__main__":
    main()
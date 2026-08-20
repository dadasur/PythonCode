import numpy as np
from sklearn.preprocessing import StandardScaler

def main():

    data = np.array([
    [25, 20000],
    [30, 40000],
    [35, 80000]
])
    
    point1 = data[0]  # [25, 20000]
    point2 = data[1]  # [30, 40000]
    distance_before = np.linalg.norm(point1 - point2)
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)

    scaled_point1 = scaled_data[0]
    scaled_point2 = scaled_data[1]

    distance_after = np.linalg.norm(scaled_point1 - scaled_point2)

    print("Point 1 before scaling:", point1)
    print("Point 2 before scaling:", point2)
    print("Euclidean distance before scaling:", distance_before)

    print("\nPoint 1 after scaling:", scaled_point1)
    print("Point 2 after scaling:", scaled_point2)
    print("Euclidean distance after scaling:", distance_after)

if __name__ == "__main__":
        main()
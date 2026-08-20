import numpy as np

def main():
      actual = np.array([1, 1, 1, 1, 0, 0, 0, 0])
      predicted = np.array([1, 1, 0, 1, 0, 1, 0, 0])

      TP = np.sum((actual == 1) & (predicted == 1))
      TN = np.sum((actual == 0) & (predicted == 0))
      FP = np.sum((actual == 0) & (predicted == 1))
      FN = np.sum((actual == 1) & (predicted == 0))

      print("True Positive  (TP):", TP)
      print("True Negative  (TN):", TN)
      print("False Positive (FP):", FP)
      print("False Negative (FN):", FN)


if __name__ == "__main__":
        main()
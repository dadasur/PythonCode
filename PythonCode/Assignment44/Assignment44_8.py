import matplotlib.pyplot as plt
import pandas as pd

def main():
     
     Border = "-"*40
     print(Border)
     print("load in data")
     print(Border)
     df = pd.read_csv("Student_Mark.csv")
     # Filter Amit's data
     amit = df[df["Name"] == "Amit"]

# Get subjects and marks
     subjects = ["Math", "Science", "English"]
     marks = amit[subjects].values.flatten()

# Plot the line chart
     plt.figure(figsize=(8, 5))
     plt.plot(subjects, marks, marker="o", color="blue", linewidth=2, markersize=8)

# Add labels and title
     plt.title("Amit's Marks Across Subjects", fontsize=14)
     plt.xlabel("Subjects", fontsize=12)
     plt.ylabel("Marks", fontsize=12)

# Add data labels on each point
     for i, mark in enumerate(marks):
      plt.text(i, mark + 1.5, str(mark), ha="center", fontsize=11)

     plt.ylim(60, 100)
     plt.grid(True, linestyle="--", alpha=0.7)
     plt.tight_layout()
     plt.show()
if __name__ == "__main__":
    main()
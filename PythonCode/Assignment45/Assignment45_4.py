#Student_Mark
import pandas as pd
import matplotlib.pyplot as plt
def MarvellousDataframe(Datapatha):
        Border = "-"*40
        print(Border)
        print("load in data")
        print(Border)
        df = pd.read_csv(Datapatha)
        sagar = df[df["Name"] == "Sagar"].iloc[0]

        # Define subjects and marks
        subjects = ["Math", "Science", "English"]
        marks = [sagar["Math"], sagar["Science"], sagar["English"]]

        # Plot pie chart
        plt.figure(figsize=(7, 7))
        plt.pie(
    marks,
    labels=subjects,
    autopct="%1.1f%%",
    startangle=140
)

plt.title("Sagar's Subject-wise Marks Distribution")
plt.tight_layout()
plt.show()
        
        
        
def main():
      MarvellousDataframe("Student_Mark.csv")

if __name__ == "__main__":
    main()
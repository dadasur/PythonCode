#Student_Mark
import pandas as pd
def MarvellousDataframe(Datapatha):
        Border = "-"*40
        print(Border)
        print("load in data")
        print(Border)
        df = pd.read_csv(Datapatha)
        df["Gender"] = ["Male", "Male", "Female"]
        average_marks = df.groupby("Gender")[["Math", "Science", "English"]].mean()
        print(average_marks)
        
        
def main():
      MarvellousDataframe("Student_Mark.csv")

if __name__ == "__main__":
    main()
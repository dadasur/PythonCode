#Student_Mark
import pandas as pd
def MarvellousDataframe(Datapatha):
        Border = "-"*40
        print(Border)
        print("load in data")
        print(Border)
        df = pd.read_csv(Datapatha)
        df["Gender"] = ["Male", "Male", "Female"]
        df = pd.get_dummies(df, columns=["Gender"], dtype=int)
        print(df)
        
def main():
      MarvellousDataframe("Student_Mark.csv")

if __name__ == "__main__":
    main()
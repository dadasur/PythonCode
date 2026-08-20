#Student_Mark
import pandas as pd
def MarvellousDataframe(Datapatha):
        Border = "-"*40
        print(Border)
        print("load in data")
        print(Border)
        df = pd.read_csv(Datapatha)
        df["Status"] = (df[["Math", "Science", "English"]].sum(axis=1) >= 250).map({
        True: "Pass",
        False: "Fail"
})

        print(df)
        
def main():
      MarvellousDataframe("Student_Mark.csv")

if __name__ == "__main__":
    main()
#Student_Mark
import pandas as pd
def MarvellousDataframe(Datapatha):
        Border = "-"*40
        print(Border)
        print("load in data")
        print(Border)
        df = pd.read_csv(Datapatha)
        df["Total"] = df[["Math", "Science", "English"]].sum(axis=1)
        df_sorted = df.sort_values(by="Total", ascending=False)
        print(df_sorted)
     
def main():
      MarvellousDataframe("Student_Mark - Copy")

if __name__ == "__main__":
    main()
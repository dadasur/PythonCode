#Student_Mark
import pandas as pd
def MarvellousDataframe(Datapatha):
        Border = "-"*40
        print(Border)
        print("load in data")
        print(Border)
        df = pd.read_csv(Datapatha)
        df.drop("English", axis=1, inplace=True)
        print(df)
        
def main():
      MarvellousDataframe("Student_Mark.csv")

if __name__ == "__main__":
    main()
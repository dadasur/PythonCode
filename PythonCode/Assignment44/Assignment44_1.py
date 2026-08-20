#Student_Mark
import pandas as pd
def MarvellousDataframe(Datapatha):
        Border = "-"*40
        print(Border)
        print("load in data")
        print(Border)
        df = pd.read_csv(Datapatha)
        print(df.shape)
        print(df.columns)

def main():
      MarvellousDataframe("Student_Mark.csv")


if __name__ == "__main__":
    main()
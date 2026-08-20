import pandas as pd
import matplotlib.pyplot as plt

def MarvellousDataframe(Datapatha):
    df = pd.read_csv(Datapatha)
    df.rename(columns={"Math": "mathematics"}, inplace=True)
    print(df)
   

def main():
    MarvellousDataframe("Student_Mark.csv")


if __name__ == "__main__":
    main()
import matplotlib.pyplot as plt
import pandas as pd

def main():
     
     Border = "-"*40
     print(Border)
     print("load in data")
     print(Border)
     df = pd.read_csv("Student_Mark.csv")
     df["Total"] = df[["Math", "Science", "English"]].sum(axis=1)
     print(df)
     plt.bar(
        df["Name"],        #valuse of x axsis
        df["Total"],       #valuse of y axsis
        width=0.6,      #widt of bar
        edgecolor = "black",
        linewidth = "1",
        alpha = 0.8,
        label = "students"
    )
     plt.title("students bar pot")
     plt.xlabel("name")
     plt.ylabel("total")
     plt.legend()
     plt.show()

if __name__ == "__main__":
    main()
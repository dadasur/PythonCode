import pandas as pd

def MarvellousDataframe(Datapatha):
    Border = "-"*40
    print(Border)
    print("Loading data")
    print(Border)
    df = pd.read_csv(Datapatha)
    df["Status"] = (df[["Math", "Science", "English"]].sum(axis=1) >= 250).map({
        True: "Pass",
        False: "Fail"
    })
    
    print(df)
    
    # Count and print passed students
    passed_count = df["Status"].value_counts()["Pass"]
    print(f"\n{Border}")
    print(f"Number of students who passed: {passed_count}")
    print(Border)

def main():
    MarvellousDataframe("Student_Mark.csv")

if __name__ == "__main__":
    main()
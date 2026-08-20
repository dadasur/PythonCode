import pandas as pd

def MarvellousDataframe(Datapatha):
    Border = "-" * 40

    print(Border)
    print("Loading data")
    print(Border)

    df = pd.read_csv(Datapatha)

    df["Status"] = (
        df[["Math", "Science", "English"]]
        .sum(axis=1)
        .ge(250)
        .map({
            True: "Pass",
            False: "Fail"
        })
    )

    print(df)

    passed_count = (df["Status"] == "Pass").sum()
    print(f"\nNumber of students who passed: {passed_count}")

    # Export the final DataFrame to a CSV file
    df.to_csv("Student_Mark_Final.csv", index=False)

    print("Final DataFrame exported to Student_Mark_Final.csv")


def main():
    MarvellousDataframe("Student_Mark.csv")


if __name__ == "__main__":
    main()
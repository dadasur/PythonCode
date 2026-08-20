import pandas as pd
import matplotlib.pyplot as plt

def MarvellousDataframe(Datapatha):
    df = pd.read_csv(Datapatha)
    # Plot histogram of Math marks
    plt.hist(
        df["Math"],
        bins=10,
        edgecolor="black",
        color="skyblue"
    )

    plt.title("Distribution of Math Marks")
    plt.xlabel("Math Marks")
    plt.ylabel("Number of Students")
    plt.grid(axis="y", alpha=0.5)
    plt.show()


def main():
    MarvellousDataframe("Student_Mark.csv")


if __name__ == "__main__":
    main()
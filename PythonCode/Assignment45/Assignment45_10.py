import pandas as pd
import matplotlib.pyplot as plt


def MarvellousDataframe(Datapatha):
    df = pd.read_csv(Datapatha)
    

    # Plot boxplot for English marks
    plt.figure(2)
    plt.boxplot(
        df["English"],
        vert=True,
        patch_artist=True,
        boxprops=dict(facecolor="lightgreen", color="black"),
        whiskerprops=dict(color="black"),
        capprops=dict(color="black"),
        medianprops=dict(color="red", linewidth=2),
        flierprops=dict(marker="o", color="red", markersize=8)
    )
    plt.title("Boxplot of English Marks")
    plt.ylabel("English Marks")
    plt.xticks([1], ["English"])
    plt.grid(axis="y", alpha=0.5)

    plt.show()


def main():
    MarvellousDataframe("Student_Mark.csv")


if __name__ == "__main__":
    main()
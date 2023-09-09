# This is the main script for IDS706 mini project 2
# In the main.py, the code will read a csv dataset and return a data summary

# the code start here

# loading packages
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def load_data(data_path):
    my_data = pd.read_csv(data_path, sep=';')
    return my_data


def data_summary(data):
    main_sum = data.describe()
    print(main_sum)


def data_visual(data):
    sns.histplot(data["Weight"], kde=True)
    mean = data['Weight'].mean()
    median = data['Weight'].median()
    quantiles = data['Weight'].quantile([.25, .5, .75])

    plt.axvline(mean, color="r")
    plt.axvline(median, linestyle='-', color="g")

    # Add vertical lines for quantiles
    for quantile in quantiles:
        plt.axvline(quantile, color='b', linestyle='-')

    plt.legend({'Mean': mean, 'Median': median, 'Quantiles': quantiles})
    plt.show()

def main():
    my_df = load_data("cars.csv")
    data_summary(my_df)
    data_visual(my_df)


if __name__ == "__main__":
    main()

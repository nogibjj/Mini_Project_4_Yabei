import polars as pl
import seaborn as sns
import matplotlib.pyplot as plt


def load_data(data_path):
    my_data = pl.read_csv(data_path, separator=";")
    return my_data


def data_summary(data):
    main_sum = data.describe()
    return main_sum


def data_visual(data):
    plt.figure(figsize=(15, 10))

    # Box Plot
    plt.subplot(2, 2, 1)
    sns.boxplot(x=data["Weight"])
    plt.title('Box Plot of Weight')

    # Violin Plot
    plt.subplot(2, 2, 2)
    sns.violinplot(x=data["Weight"])
    plt.title('Violin Plot of Weight')

    # CDF Plot
    plt.subplot(2, 2, 3)
    sns.ecdfplot(data=data, x="Weight")
    plt.title('CDF Plot of Weight')

    # KDE Plot
    plt.subplot(2, 2, 4)
    sns.kdeplot(data=data, x="Weight", fill=True)
    plt.title('KDE Plot of Weight')

    plt.tight_layout()
    plt.show()

def main():
    my_df = load_data("cars.csv")
    print(data_summary(my_df))
    data_visual(my_df)


if __name__ == "__main__":
    main()
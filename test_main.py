
from main import data_summary
import pandas as pd

# Load the dataset
my_df = pd.read_csv('cars.csv', sep = ';')


def test_summary(data):
    summary = data_summary(data)

    mean = data['Weight'].mean()
    median = data['Weight'].median()

    assert mean == summary.loc['mean', 'Weight'], "Mean test failed"
    assert median == summary.loc['50%', 'Weight'], "Median test failed"
    print("All Test passed!")

if __name__ == "__main__":
    test_summary(my_df)

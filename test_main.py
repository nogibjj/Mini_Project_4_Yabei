
from main import data_summary
import pandas as pd

def test_summary():
    my_df = pd.read_csv('cars.csv', sep=';')
    summary = data_summary(my_df)
    mean = my_df['Weight'].mean()
    median = my_df['Weight'].median()
    assert mean == summary.loc['mean', 'Weight'], "Mean test failed"
    assert median == summary.loc['50%', 'Weight'], "Median test failed"

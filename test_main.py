from main import data_summary

import pandas as pd

my_df = pd.read_csv('cars.csv')
def test_summary(data):
    summary = data_summary(data)
    mpg_mean = data['MPG'].mean()
    mpg_median = data['MPG'].median()
    assert mpg_mean == summary.loc['mean', 'MPG']
    assert mpg_median == summary.loc['median', 'MPG']

test_summary(my_df)
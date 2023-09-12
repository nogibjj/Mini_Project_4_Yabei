from main import data_summary, load_data, data_visual
import polars as pl

def test_summary():
    my_df = pl.read_csv('cars.csv', separator=';')
    summary = data_summary(my_df)
    mean = my_df['Weight'].mean()
    median = my_df['Weight'].median()
    assert mean == summary['mean']['Weight'], "Mean test failed"
    assert median == summary['50%']['Weight'], "Median test failed"

def test_load_data():
    data_path = 'cars.csv'
    df = load_data(data_path)
    assert isinstance(df, pl.DataFrame), "load_data should return a DataFrame"
    assert not df.shape[0] == 0, "DataFrame should not be empty"

def test_data_visual():
    data_path = 'cars.csv'
    df = load_data(data_path)
    try:
        data_visual(df)
    except Exception as e:
        assert False, f"data_visual function raised an exception: {e}"

# IDS706 Mini Project 2

This project provides a Python script that used polars and reads a CSV dataset named cars.csv, returns a summary of the data, and visualizes it using various plots.

## Getting Started

You need to have Python installed on your machine. You can download it from [here](https://www.python.org/downloads/). The code is written in Python 3.

The following Python packages are also required:
- `polars`
- `seaborn`
- `matplotlib`

You can install these packages using pip:

```bash
pip install polars seaborn matplotlib
```

## File Description

`main.py`: This is the main script file that contains all the functions for loading the data, summarizing it, and visualizing it.

## How to Run

You can run the script by navigating to the directory containing the `main.py` file in your terminal and running the command:

```bash
python main.py
```

## Functions

The `main.py` script contains the following functions:

- `load_data(data_path)`: This function reads a CSV file from the specified path and returns it as a Polars DataFrame. The data is expected to be semicolon-separated.

- `data_summary(data)`: This function takes a Polars DataFrame as input and returns a summary of the data. The summary includes the count, mean, standard deviation, minimum and maximum values, and the 25th, 50th, and 75th percentiles for each column.

- `data_visual(data)`: This function takes a Polars DataFrame as input and generates four types of plots for the "Weight" column of the data: a box plot, a violin plot, a cumulative distribution function (CDF) plot, and a kernel density estimate (KDE) plot.

- `main()`: This is the main function that calls the other functions. It loads the data from the "cars.csv" file, prints the data summary, and generates the plots.

## Note

The `main.py` script is currently set to load data from a file named "cars.csv" in the same directory, and it specifically visualizes the "Weight" column. If you wish to use this script with a different dataset or visualize a different column, you will need to modify the `main()` function appropriately.

## Output Preview
![Mini_project3_image](https://github.com/yabeizeng1121/Mini_project_3/assets/143656459/ee8f9c15-128f-441d-8273-86fa8d9a2c1c)


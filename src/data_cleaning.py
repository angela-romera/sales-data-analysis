import pandas as pd
from utils.quick_plots import boxplot_per_column, histogram_per_column


def check_null_values(df):
    try:
        if df.isnull().sum().sum() > 0:
            null_counts = df.isnull().sum()
            null_percentage = (df.isnull().sum() / len(df)) * 100

            null_summary = pd.DataFrame({
                "Column": null_counts[null_counts > 0].index,
                "num null values": null_counts[null_counts > 0].values,
                "% null values": null_percentage[null_percentage > 0].values
            })

            return null_summary

        else:
            return pd.DataFrame()

    except:
        print('Error getting null vals')


def df_summary(df):
    try:
        print("DataFrame summary:")
        print("---------------------")
        print(f"\nColumn types:")
        print(df.dtypes)
        print(f"\nNull values:")
        result = check_null_values(df)
        if not result.empty:
            print(result)
        else:
            print("There are no null values")

    except:
        print('Error getting df summary')


def plot_analysis(df):
    boxplot_per_column(df)
    histogram_per_column(df)

import pandas as pd

from src.data_cleaning import df_summary, check_null_values, plot_analysis


def main():
    df = pd.read_csv("data/Sales Data 2.csv", sep=",", quotechar='"')
    # df_summary(df)

    # Remove first column
    df = df.drop(df.columns[0], axis=1)
    # df_summary(df)

    # Convert Hour column from int to time format
    df['Hour'] = pd.to_datetime(df['Hour'], format='%H').dt.time
    # df_summary(df)

    # Remove rows w/ nan
    result = check_null_values(df)
    if not result.empty:
        df.dropna(inplace=True)
    # df_summary(df)

    # Deal w/ duplicates
    df = df.groupby(['Product', 'Order Date', 'Purchase Address', 'Month', 'City', 'Hour']).agg({
        'Quantity Ordered': 'sum',
        'Sales': 'sum',
        'Price Each': 'mean',
        'Order ID': 'first'
    }).reset_index()
    df_summary(df)

    # Filter numeric columns
    df_numeric = df.select_dtypes(include=['number'])
    df_numeric = df_numeric.drop(columns=['Order ID'])

    plot_analysis(df_numeric)


if __name__ == "__main__":
    main()

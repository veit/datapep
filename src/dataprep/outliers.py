import pandas as pd


def find_outliers():
    df = pd.read_csv(
        "https://raw.githubusercontent.com/kjam/data-cleaning-101/master/data/iot_example_with_nulls.csv"
    )
    heartrate = df["heartrate"]
    heartrate_mean = heartrate.mean()
    heartrate_min = heartrate_mean-10
    heartrate_max = heartrate_mean+10
    df_min = df[heartrate < heartrate_min]
    df_max = df[heartrate > heartrate_max]
    outliers = pd.concat(df_min, df_max)
    return outliers
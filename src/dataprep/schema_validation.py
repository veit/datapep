from pathlib import Path

import pandas as pd

from tdda.constraints import detect_df, discover_df, verify_df


def discover_schema():
    refernce_df = pd.read_csv(
        "https://raw.githubusercontent.com/kjam/data-cleaning-101/master/data/iot_example.csv",
        )
    constrains = discover_df(refernce_df)
    with Path.open("iot_example.json", "w") as f:
        f.write(constrains.to_json())


new_df = pd.read_csv(
    "https://raw.githubusercontent.com/kjam/data-cleaning-101/master/data/iot_example_with_nulls.csv"
)

def verify_new_df():
    verified = verify_df(new_df, "iot_example.json")
    print(str(verified))

def show_invalid_records():
    detected = detect_df(new_df, "iot_example.json")
    detected_index = detected.detected().index
    return new_df[new_df.index.isin(detected_index)]

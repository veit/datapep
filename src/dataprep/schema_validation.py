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

"""Import-Modul dür das Lesen und Validieren der Daten"""

import pandas as pd

customers = pd.read_csv(
    "https://raw.githubusercontent.com/kjam/data-cleaning-101/master/data/customer_data_duped.csv",
    encoding="utf-8",
)
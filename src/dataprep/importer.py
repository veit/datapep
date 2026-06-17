"""Import-Modul dür das Lesen und Validieren der Daten"""

import pandas as pd

customers = pd.read_csv(
    "https://raw.githubusercontent.com/kjam/data-cleaning-101/master/data/customer_data_duped.csv",
    encoding="utf-8",
)

new_customers = pd.read_csv(
    "https://raw.githubusercontent.com/kjam/data-cleaning-101/master/data/customer_data_duped.csv",
    encoding="utf-8",
)

customers_shape = customers.shape

if customers_shape[0] == 0:
    print("Der DataFrame enthält keine Datensätze")

if customers_shape[1] != 8:
    print("WARNUNG: Der DataFrame enthält nicht die erwarteten acht Spalten")

if customers_shape[1] == 8:
    print("Der DataFrame enthält die erwarteten acht Spalten")

def add_data(existing_df, new_df):
    """Zusammenführen von Datensätzen

    >>> from dataprep import importer
    >>> importer.add_data(importer.customers, importer.new_customers)
    """
    combined_df = pd.concat([existing_df, new_df])
    return combined_df


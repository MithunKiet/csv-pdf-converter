import pandas as pd

def read_csv(path: str) -> pd.DataFrame:
    """
    CSV file ko pandas DataFrame me read karta hai.
    """
    return pd.read_csv(path)

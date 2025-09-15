import pandas as pd

def normalize_assets(df: pd.DataFrame) -> pd.DataFrame:
    """
    DataFrame ko normalize karta hai:
    - Status column ko title case me convert
    - Null values ko 'Unknown' se fill
    """
    df = df.copy()
    if "Status" in df.columns:
        df["Status"] = df["Status"].astype(str).str.title().fillna("Unknown")
    return df

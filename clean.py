"""
clean.py
Module for loading and cleaning the Netflix dataset.
"""

import pandas as pd


def load_data(filepath: str) -> pd.DataFrame:
    """
    Load CSV file into a DataFrame.

    Args:
        filepath: Path to the CSV file.

    Returns:
        Raw DataFrame.
    """
    df = pd.read_csv(filepath, encoding="latin1", on_bad_lines='skip')
    print(f"Loaded {len(df):,} rows and {len(df.columns)} columns.")
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the DataFrame by removing duplicates,
    stripping whitespace, and standardizing column names.

    Args:
        df: Raw DataFrame.

    Returns:
        Cleaned DataFrame.
    """
    # remove duplicate rows
    df = df.drop_duplicates()

    # standardize column names to lowercase with underscores
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
    )

    # strip whitespace from string columns
    str_cols = df.select_dtypes(include="object").columns
    df[str_cols] = df[str_cols].apply(lambda col: col.str.strip())

    # fill missing numeric values with column median
    num_cols = df.select_dtypes(include="number").columns
    df[num_cols] = df[num_cols].fillna(df[num_cols].median())

    print(f"After cleaning: {len(df):,} rows remaining.")
    print(f"Missing values:\n{df.isnull().sum()}\n")
    return df


def save_data(df: pd.DataFrame, filepath: str) -> None:
    """
    Save cleaned DataFrame to CSV.

    Args:
        df: Cleaned DataFrame.
        filepath: Destination path.
    """
    df.to_csv(filepath, index=False)
    print(f"Saved cleaned data to: {filepath}") 
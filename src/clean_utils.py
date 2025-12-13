import pandas as pd
from sklearn.model_selection import train_test_split

def clean_sleep_data(df: pd.DataFrame, random_state: int = 522) -> pd.DataFrame:
    """
    Cleans the sleep data by selecting specific columns, renaming them, 
    filling missing values, and adding a 'train' column for data splitting.

    Parameters
    ----------
    df : pd.DataFrame
        The raw dataframe containing sleep data.
    random_state : int, optional
        Random state for the train-test split, by default 522.

    Returns
    -------
    pd.DataFrame
        The cleaned dataframe with the new 'train' column.
    
    Raises
    ------
    ValueError
        If required columns are missing from the input dataframe.
    """
    df_clean = df.copy()

    # Columns to keep
    target_columns = [
        "Person ID",
        "Sleep Duration",
        "Quality of Sleep",
        "Sleep Disorder",
        "Stress Level",
    ]

    # Check if all target columns exist
    if not set(target_columns).issubset(df.columns):
        missing = set(target_columns) - set(df.columns)
        raise ValueError(f"The following required columns are missing from the dataframe: {missing}")

    df_clean = df_clean[target_columns]

    # renaming columns using the camel_syntax
    name_conversion_dict = {
        "Person ID": "person_id",
        "Sleep Duration": "sleep_duration",
        "Quality of Sleep": "sleep_quality",
        "Sleep Disorder": "sleep_disorder",
        "Stress Level": "stress_level",
    }

    df_clean = df_clean.rename(columns=name_conversion_dict)

    df_clean["sleep_disorder"] = df_clean["sleep_disorder"].fillna("No Disorder")

    # Perform train-test split to identify training indices
    # The split parameters match the notebook: test_size=0.2
    if len(df_clean) > 1:
        train_df, _ = train_test_split(df_clean, test_size=0.2, random_state=random_state)
        
        # Create 'train' column: 1 for train, 0 for test
        df_clean["train"] = 0
        df_clean.loc[train_df.index, "train"] = 1
    else:
        # Handle edge case where dataframe is too small to split
        df_clean["train"] = 1

    return df_clean

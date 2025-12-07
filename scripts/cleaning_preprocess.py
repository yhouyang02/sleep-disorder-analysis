import pandas as pd
import click
import os
from sklearn.model_selection import train_test_split

@click.command()
@click.option('--source', default='data/raw/sleep_raw.csv', help='The path to the raw data file')
@click.option('--dest', default='data/processed/clean_sleep_data.csv', help='The path to save the cleaned data file')
def cleaning_preprocess(source, dest):
    """
    Reads data from the source path, processes it, adds a 'train' column indicating
    split (1 for train, 0 for test), and saves the result to the destination path.
    """
    try:
        df = pd.read_csv(source)
    except FileNotFoundError:
        print(f"Error: The file '{source}' was not found.")
        return

    df_clean = df.copy()
    
    # Columns to keep
    target_columns = [
        "Person ID",
        "Sleep Duration",
        "Quality of Sleep",
        "Sleep Disorder",
        "Stress Level"
    ]
    
    # Check if all target columns exist
    if not set(target_columns).issubset(df.columns):
        missing = set(target_columns) - set(df.columns)
        print(f"Error: The following required columns are missing from the source file: {missing}")
        return

    df_clean = df_clean[target_columns]

    # renaming columns using the camel_syntax
    name_conversion_dict = {
        "Person ID": 'person_id',
        "Sleep Duration": 'sleep_duration',
        "Quality of Sleep": 'sleep_quality',
        "Sleep Disorder": 'sleep_disorder',
        "Stress Level": 'stress_level'
    }

    df_clean = df_clean.rename(columns=name_conversion_dict)

    df_clean["sleep_disorder"] = df_clean["sleep_disorder"].fillna("No Disorder")
    
    # Perform train-test split to identify training indices
    # The split parameters match the notebook: test_size=0.2, random_state=522
    train_df, _ = train_test_split(df_clean, test_size=0.2, random_state=522)
    
    # Create 'train' column: 1 for train, 0 for test
    df_clean['train'] = 0
    df_clean.loc[train_df.index, 'train'] = 1
    
    # Ensure destination directory exists
    os.makedirs(os.path.dirname(dest), exist_ok=True)

    try:
        # Save full cleaned data with split info
        df_clean.to_csv(dest, index=False)
        print(f"Successfully cleaned data, added split column, and saved to '{dest}'")
        
    except Exception as e:
        print(f"Error saving file to '{dest}': {e}")

if __name__ == "__main__":
    cleaning_preprocess()
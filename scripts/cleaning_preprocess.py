import pandas as pd
import path
import click

@click.comand()
@click.option('--source',default='data/raw/sleep_raw.csv',help='The path to the raw data file')
@click.option('--dest', default="data/processed/clean_sleep_data.csv", help='The path to save the cleaned data file')

def cleaning_preprocess(file_path: str):
    """
    Normalizes a file path by replacing backslashes with forward slashes.

    Args:
        file_path: The original file path string.

    Returns:
        The normalized file path string with forward slashes.
    """
    df = pd.read_csv(path(file_path))
    df_clean = df.copy()
    df_clean = df_clean[[
    "Person ID",
    "Sleep Duration",
    "Quality of Sleep",
    "Sleep Disorder",
    "Stress Level"
    ]]

    # renaming columns using the camel_syntax
    name_conversion_dict = {
    "Person ID": 'person_id',
    "Sleep Duration": 'sleep_duration',
    "Quality of Sleep": 'sleep_quality',
    "Sleep Disorder": 'sleep_disorder',
    "Stress Level": 'stress_level'
    }

    df_clean = df_clean.rename(columns=name_conversion_dict)

    df_clean[["sleep_disorder"]] = df_clean[["sleep_disorder"]].fillna("No Disorder")

    return df_clean

if __name__ == "__main__":
    # Example usage
    default_path = "data/raw.csv"
    #run the script with the default path
    df=cleaning_preprocess(default_path)
    df.to_csv("data/processed/clean_sleep_data.csv", index=False)




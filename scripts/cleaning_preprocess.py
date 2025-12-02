import pandas as pd
import path

def cleaning_preprocess(file_path: str):
    """
    Normalizes a file path by replacing backslashes with forward slashes.

    Args:
        file_path: The original file path string.

    Returns:
        The normalized file path string with forward slashes.
    """
    df = pd.read_csv(file_path)
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

    df_clean.sample(7).reset_index(drop=True)

    return 

if __name__ == "__main__":
    # Example usage
    default_path = "data/raw.csv"
    #run the script with the default path
    cleaning_preprocess(default_path)
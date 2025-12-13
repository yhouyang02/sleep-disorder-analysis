import pandas as pd
import click
import os
import sys

# Add the project root to sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from src.clean_utils import clean_sleep_data


@click.command()
@click.option(
    "--source",
    default="data/raw/sleep_data_raw.csv",
    help="The path to the raw data file",
)
@click.option(
    "--dest",
    default="data/processed/sleep_data_clean.csv",
    help="The path to save the cleaned data file",
)
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

    try:
        df_clean = clean_sleep_data(df)
    except ValueError as e:
        print(f"Error: {e}")
        return

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

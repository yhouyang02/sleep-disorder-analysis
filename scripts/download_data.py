# download_data.py
# author: Norton Yu
# date: 2025-12-02

import sys
from pathlib import Path
import click


ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from src.download_utils import download_csv


@click.command()
@click.option(
    "--input-path",
    type=str,
    required=True,
    default="https://raw.githubusercontent.com/Muhanad-husn/Sleep-Health-and-Lifestyle/main/data.csv",
    help="URL or local path to the raw CSV data.",
)
@click.option(
    "--output-path",
    type=str,
    required=True,
    default="data/raw/sleep_data_raw.csv",
    help="Where to save the downloaded data, e.g. data/raw/sleep_data_raw.csv",
)
def main(input_path, output_path):
    """Download CSV data from a URL or local path and save it to the specified output path."""
    try:
        saved_path = download_csv(input_path, output_path)
        print(f"Data successfully downloaded and saved to: {saved_path}")
    except Exception as e:
        print(f"An error occurred while downloading the data: {e}")


if __name__ == "__main__":
    main()

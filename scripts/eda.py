import click
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from src.eda_utils import perform_eda


@click.command()
@click.option(
    "--input-file",
    default="data/processed/sleep_data_clean.csv",
    help="Path to the cleaned data file",
)
@click.option(
    "--output-dir", default="../results", help="Directory to save the figures"
)
def main(input_file, output_dir):
    """Perform exploratory data analysis and save visualizations."""
    perform_eda(input_file, output_dir)


if __name__ == "__main__":
    main()

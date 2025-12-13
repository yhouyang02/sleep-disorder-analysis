import click
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
def main():
    """Perform exploratory data analysis and save visualizations."""
    perform_eda()


if __name__ == "__main__":
    main()

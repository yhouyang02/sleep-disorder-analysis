# download_data.py
# author: Norton Yu
# date: 2025-12-02

import os
from urllib.parse import urlparse
import click
import pandas as pd


@click.command()
@click.option(
    "--input-path",
    type=str,
    required=True,
    help="URL or local path to the raw CSV data.",
)
@click.option(
    "--output-path",
    type=str,
    required=True,
    help="Where to save the downloaded data, e.g. data/raw/sleep_raw.csv",
)
def main(input_path, output_path):
    """Download or copy a raw CSV file and save it locally."""

    # Create output directory if needed
    out_dir = os.path.dirname(output_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)

    # Check if input-path is a URL
    parsed = urlparse(input_path)
    is_url = parsed.scheme in {"http", "https"}

    if is_url:
        # Download CSV from URL
        df = pd.read_csv(input_path)
        df.to_csv(output_path, index=False)
    else:
        # Copy local CSV
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"{input_path} not found.")
        df = pd.read_csv(input_path)
        df.to_csv(output_path, index=False)

    click.echo(f"Saved data to {output_path}")


if __name__ == "__main__":
    main()

# download_data.py
# author: Norton Yu
# date: 2025-12-02

import os
import ssl
import urllib.request
from urllib.parse import urlparse
import click
import pandas as pd


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
        # Handle SSL certificate verification
        try:
            # Try with default SSL context first
            df = pd.read_csv(input_path)
        except Exception as e:
            if "CERTIFICATE_VERIFY_FAILED" in str(e) or "SSL" in str(e):
                # If SSL fails, try with unverified context (less secure but works)
                # Note: This is a workaround for macOS SSL certificate issues
                # Create an unverified SSL context
                ssl_context = ssl.create_default_context()
                ssl_context.check_hostname = False
                ssl_context.verify_mode = ssl.CERT_NONE
                # Use urllib with the SSL context to download
                with urllib.request.urlopen(
                    input_path, context=ssl_context
                ) as response:
                    df = pd.read_csv(response)
            else:
                raise
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

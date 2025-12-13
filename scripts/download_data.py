# download_data.py
# author: Norton Yu
# date: 2025-12-02

import os
import ssl
import urllib.request
from urllib.parse import urlparse
import click
import pandas as pd

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
    download_csv(input_path, output_path)


if __name__ == "__main__":
    main()

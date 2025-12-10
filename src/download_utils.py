import os
from urllib.parse import urlparse
import pandas as pd


def download_csv(input_path: str, output_path: str) -> str:
    """
    Download or copy a CSV file from a URL or local path and save it to output_path.

    Parameters
    ----------
    input_path : str
        URL or local path to the raw CSV data.
    output_path : str
        Local path where the CSV should be saved.

    Returns
    -------
    str
        The path where the data was saved.
    """
    # Create output directory if needed
    out_dir = os.path.dirname(output_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)

    # Check if input_path is a URL
    parsed = urlparse(input_path)
    is_url = parsed.scheme in {"http", "https"}

    if is_url:
        df = pd.read_csv(input_path)
        df.to_csv(output_path, index=False)
    else:
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"{input_path} not found.")
        df = pd.read_csv(input_path)
        df.to_csv(output_path, index=False)

    return output_path

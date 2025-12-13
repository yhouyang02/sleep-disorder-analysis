import os
import pandas as pd
import pytest

from src.download_utils import download_csv


def test_download_csv_local_file(tmp_path):
    """download_csv should save the same data to the output path for a local file."""
    input_df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
    input_file = tmp_path / "input.csv"
    output_file = tmp_path / "output.csv"
    input_df.to_csv(input_file, index=False)

    result_path = download_csv(str(input_file), str(output_file))

    # Assert
    assert os.path.exists(result_path)
    result_df = pd.read_csv(result_path)
    pd.testing.assert_frame_equal(result_df, input_df)


def test_download_csv_missing_local_file_raises(tmp_path):
    """download_csv should raise FileNotFoundError when local input file does not exist."""
    missing_input = tmp_path / "does_not_exist.csv"
    output_file = tmp_path / "output.csv"

    with pytest.raises(FileNotFoundError):
        download_csv(str(missing_input), str(output_file))
    
def test_download_csv_empty_input(tmp_path):
    """download_csv should still work with empty case."""
    input_df = pd.DataFrame({"a": []})
    input_file = tmp_path / "empty.csv"
    output_file = tmp_path / "empty_out.csv"
    input_df.to_csv(input_file, index=False)

    result_path = download_csv(str(input_file), str(output_file))

    # Assert
    assert os.path.exists(result_path)
    result_df = pd.read_csv(result_path)

    # Check for same columns, zero rows
    assert list(result_df.columns) == list(input_df.columns)
    assert len(result_df) == 0

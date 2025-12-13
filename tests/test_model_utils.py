import pytest
import pandas as pd
import os
import matplotlib
import sys
from pathlib import Path

matplotlib.use("Agg")

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))


from src.model_utils import save_df_as_png


@pytest.fixture
def sample_df():
    return pd.DataFrame(
        {"Name": ["Alice", "Bob"], "Age": [25, 30], "Score": [88.5, 92.0]}
    )


# Good input
def test_save_df_as_png_valid(sample_df, tmp_path):
    """
    Test that a valid DataFrame and valid path create a file.
    """
    output_file = tmp_path / "test_table.png"

    save_df_as_png(sample_df, str(output_file), title="Test Title")

    assert os.path.exists(output_file)
    assert os.path.getsize(output_file) > 0


# Invalid data type
def test_save_df_as_png_bad_input():
    """
    Test that passing a non-DataFrame object raises an AttributeError.
    Since the function does not validate input types explicitly,
    Python will raise an error when accessing .columns or .values.
    """
    bad_input = "Not a dataframe"

    with pytest.raises(AttributeError):
        save_df_as_png(bad_input, "will_fail.png")


# System/IO error
def test_save_df_as_png_io_error(sample_df, capsys):
    """
    Test the internal try/except block by providing an invalid file path.
    The function catches the exception and prints an error message.
    """
    invalid_path = "/non_existent_directory/image.png"

    save_df_as_png(sample_df, invalid_path)

    captured = capsys.readouterr()

    assert "Error saving table" in captured.out
    assert not os.path.exists(invalid_path)

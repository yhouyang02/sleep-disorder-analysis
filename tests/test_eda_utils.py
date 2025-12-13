"""
Tests for scripts/eda.py - Exploratory Data Analysis script

some of the tests performed in this file are:
- Test good input: valid data with all required columns creates output file.
- Test good input: filters training data correctly when train column exists.
- Test bad input: missing train column uses all data with warning.
- Test bad input: empty dataframe still creates output file.
- Test bad input: single row dataframe (edge case).
- Test error input: missing input file should print error message.
- Test error input: missing required columns should raise KeyError.
"""

import sys
import pandas as pd
import pytest
from pathlib import Path

# Add project root to path
ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from src.eda_utils import perform_eda


@pytest.fixture
def sample_data():
    """Create sample data for testing."""
    return pd.DataFrame(
        {
            "person_id": [1, 2, 3, 4, 5],
            "sleep_duration": [7.5, 6.0, 8.0, 5.5, 7.0],
            "sleep_quality": [8, 6, 9, 5, 7],
            "sleep_disorder": [
                "No Disorder",
                "Insomnia",
                "No Disorder",
                "Sleep Apnea",
                "No Disorder",
            ],
            "stress_level": [4, 7, 3, 8, 5],
            "train": [1, 1, 0, 1, 0],
        }
    )


def test_good_input_creates_output_file(sample_data, tmp_path):
    """Test good input: valid data with all required columns creates output file."""
    input_file = tmp_path / "test_data.csv"
    sample_data.to_csv(input_file, index=False)

    output_dir = tmp_path / "output"
    perform_eda(str(input_file), str(output_dir))

    output_file = output_dir / "eda_summary.png"
    assert output_file.exists(), "Output PNG file should be created"
    assert output_file.stat().st_size > 1000, "Output file should have reasonable size"


def test_good_input_filters_training_data(sample_data, tmp_path, capsys):
    """Test good input: filters training data correctly when train column exists."""
    input_file = tmp_path / "test_data.csv"
    sample_data.to_csv(input_file, index=False)

    output_dir = tmp_path / "output"
    perform_eda(str(input_file), str(output_dir))

    captured = capsys.readouterr()
    assert "Using training subset" in captured.out
    assert "3 samples" in captured.out  # 3 rows with train=1


def test_bad_input_missing_train_column(tmp_path, capsys):
    """Test bad input: missing train column uses all data with warning."""
    data_no_train = pd.DataFrame(
        {
            "sleep_duration": [7.5, 6.0, 8.0],
            "sleep_quality": [8, 6, 9],
            "sleep_disorder": ["No Disorder", "Insomnia", "No Disorder"],
            "stress_level": [4, 7, 3],
        }
    )

    input_file = tmp_path / "test_data.csv"
    data_no_train.to_csv(input_file, index=False)

    output_dir = tmp_path / "output"
    perform_eda(str(input_file), str(output_dir))

    captured = capsys.readouterr()
    assert "Warning: 'train' column not found" in captured.out

    # Should still create output file
    output_file = output_dir / "eda_summary.png"
    assert output_file.exists()


def test_bad_input_empty_dataframe(tmp_path):
    """Test bad input: empty dataframe still creates output file."""
    empty_df = pd.DataFrame(
        {
            "sleep_duration": [],
            "sleep_quality": [],
            "sleep_disorder": [],
            "stress_level": [],
            "train": [],
        }
    )

    input_file = tmp_path / "empty_data.csv"
    empty_df.to_csv(input_file, index=False)

    output_dir = tmp_path / "output"
    perform_eda(str(input_file), str(output_dir))

    # Should not raise error and should create output file
    output_file = output_dir / "eda_summary.png"
    assert output_file.exists()


def test_bad_input_single_row(tmp_path):
    """Test bad input: single row dataframe (edge case)."""
    single_row_df = pd.DataFrame(
        {
            "sleep_duration": [7.5],
            "sleep_quality": [8],
            "sleep_disorder": ["No Disorder"],
            "stress_level": [4],
            "train": [1],
        }
    )

    input_file = tmp_path / "single_row.csv"
    single_row_df.to_csv(input_file, index=False)

    output_dir = tmp_path / "output"
    perform_eda(str(input_file), str(output_dir))

    # Should create output file (uses scatterplot instead of regplot)
    output_file = output_dir / "eda_summary.png"
    assert output_file.exists()


def test_error_input_missing_file(tmp_path, capsys):
    """Test error input: missing input file should print error message."""
    missing_file = tmp_path / "nonexistent.csv"
    output_dir = tmp_path / "output"

    perform_eda(str(missing_file), str(output_dir))

    captured = capsys.readouterr()
    assert "Error: Input file" in captured.out
    assert "not found" in captured.out


def test_error_input_missing_columns(tmp_path):
    """Test error input: missing required columns should raise KeyError."""
    incomplete_df = pd.DataFrame(
        {
            "sleep_duration": [7.5, 6.0],
            "sleep_quality": [8, 6],
            "train": [1, 1],
            # Missing sleep_disorder and stress_level
        }
    )

    input_file = tmp_path / "incomplete_data.csv"
    incomplete_df.to_csv(input_file, index=False)

    output_dir = tmp_path / "output"

    with pytest.raises(KeyError):
        perform_eda(str(input_file), str(output_dir))

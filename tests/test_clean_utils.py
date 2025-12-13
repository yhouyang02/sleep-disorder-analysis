import pandas as pd
import pytest
import numpy as np
from src.clean_utils import clean_sleep_data


@pytest.fixture
def raw_data():
    """Provides a small sample dataframe resembling the raw sleep data."""
    return pd.DataFrame(
        {
            "Person ID": [1, 2, 3, 4, 5],
            "Sleep Duration": [7.0, 6.0, 8.0, 5.5, 7.5],
            "Quality of Sleep": [8, 6, 9, 5, 8],
            "Sleep Disorder": [np.nan, "Insomnia", np.nan, "Sleep Apnea", "Insomnia"],
            "Stress Level": [3, 8, 2, 9, 4],
            "Extra Column": ["A", "B", "C", "D", "E"],  # Should be dropped
        }
    )


def test_clean_sleep_data_good_input(raw_data):
    """Test that the function cleans the data correctly under normal conditions."""
    cleaned_df = clean_sleep_data(raw_data)

    # Check if extra column is dropped
    assert "Extra Column" not in cleaned_df.columns

    # Check renamed columns
    expected_cols = {
        "person_id",
        "sleep_duration",
        "sleep_quality",
        "sleep_disorder",
        "stress_level",
        "train",
    }
    assert set(cleaned_df.columns) == expected_cols

    # Check NA filling
    assert not cleaned_df["sleep_disorder"].isnull().any()
    assert (cleaned_df["sleep_disorder"] == "No Disorder").sum() == 2  # 2 NaNs in input

    # Check train column exists and has 0s and 1s (or just 0/1 logic)
    assert cleaned_df["train"].isin([0, 1]).all()
    # With 5 rows and 0.2 split, usually split is consistent if random_state is fixed
    # But exact split depends on version/algo, so checking basic property is safer
    assert cleaned_df["train"].sum() > 0  # Should have some training data


def test_clean_sleep_data_missing_columns():
    """Test that the function raises ValueError when required columns are missing."""
    bad_df = pd.DataFrame(
        {
            "Person ID": [1, 2],
            "Sleep Duration": [7.0, 6.0],
            # Missing other required columns
        }
    )

    with pytest.raises(ValueError, match="missing from the dataframe"):
        clean_sleep_data(bad_df)


def test_clean_sleep_data_empty_dataframe():
    """Test that the function handles empty dataframes gracefully (or raises expected error if logical)."""
    # If the dataframe is empty but has columns, it should pass but be empty
    empty_df = pd.DataFrame(
        columns=[
            "Person ID",
            "Sleep Duration",
            "Quality of Sleep",
            "Sleep Disorder",
            "Stress Level",
        ]
    )

    cleaned_df = clean_sleep_data(empty_df)

    assert cleaned_df.empty
    assert "train" in cleaned_df.columns


def test_clean_sleep_data_small_dataframe():
    """Test edge case with very few rows where splitting might behave effectively differently."""
    small_df = pd.DataFrame(
        {
            "Person ID": [1],
            "Sleep Duration": [8.0],
            "Quality of Sleep": [9],
            "Sleep Disorder": [np.nan],
            "Stress Level": [2],
        }
    )

    cleaned_df = clean_sleep_data(small_df)

    # If only 1 row, our logic sets train=1
    assert len(cleaned_df) == 1
    assert cleaned_df.iloc[0]["train"] == 1

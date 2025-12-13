import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns
import click
import os

from sklearn.model_selection import cross_validate
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, r2_score


def save_df_as_png(df, filename, title=None):
    """
    Saves a pandas DataFrame as a PNG table.
    """
    fig, ax = plt.subplots(figsize=(len(df.columns) * 2.5, len(df) * 0.8 + 1))
    ax.axis("off")

    # Create table
    table = ax.table(
        cellText=df.values, colLabels=df.columns, loc="center", cellLoc="center"
    )

    # Style table
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1, 1.5)

    if title:
        plt.title(title, fontsize=16, fontweight="bold", pad=20)

    plt.tight_layout()
    try:
        plt.savefig(filename, bbox_inches="tight", dpi=150)
        print(f"Table saved to '{filename}'")
    except Exception as e:
        print(f"Error saving table '{filename}': {e}")
    finally:
        plt.close(fig)


@click.command()
@click.option(
    "--input-file",
    default="data/processed/sleep_data_clean.csv",
    help="Path to the cleaned data file",
)
@click.option(
    "--output-prefix",
    default="results/model_analysis",
    help="Prefix for output files (e.g. results/this_analysis)",
)
def run_model(input_file, output_prefix):
    """
    Performs modeling analysis:
    1. Loads data and splits into train/test based on 'train' column.
    2. Trains a Ridge regression pipeline with CV.
    3. Evaluates on test set.
    4. Generates tables and plots.
    """
    # 1. Load Data
    try:
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        return

    # Ensure output directory exists
    output_dir = os.path.dirname(output_prefix)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    # Split Data
    if "train" not in df.columns:
        print("Error: 'train' column missing from input file. Cannot split data.")
        return

    train_df = df[df["train"] == 1].copy()
    test_df = df[df["train"] == 0].copy()

    target_col = "stress_level"
    drop_cols = [target_col, "train", "person_id"]

    # Drop person_id if it exists, it's not a feature
    cols_to_drop = [c for c in drop_cols if c in df.columns]

    X_train = train_df.drop(columns=cols_to_drop)
    y_train = train_df[target_col]

    X_test = test_df.drop(columns=cols_to_drop)
    y_test = test_df[target_col]

    print(f"Training shapes: X={X_train.shape}, y={y_train.shape}")
    print(f"Testing shapes: X={X_test.shape}, y={y_test.shape}")

    # 2. Define Pipeline
    # Note: remainder='passthrough' is crucial to keep sleep_quality which isn't transformed
    preprocesser = make_column_transformer(
        (StandardScaler(), ["sleep_duration"]),
        (OneHotEncoder(), ["sleep_disorder"]),
        remainder="passthrough",
    )

    ridge_pipe = make_pipeline(preprocesser, Ridge(alpha=1.0))

    # 3. Cross-Validation
    print("Running Cross-Validation...")
    cv_results = cross_validate(
        ridge_pipe,
        X_train,
        y_train,
        cv=5,
        scoring=["neg_mean_squared_error", "r2"],
        return_train_score=True,
    )

    cv_results_df = pd.DataFrame(cv_results).rename(
        columns={
            "test_neg_mean_squared_error": "test_neg_MSE",
            "train_neg_mean_squared_error": "train_neg_MSE",
        }
    )

    # Calculate means for summary
    cv_summary = cv_results_df.mean().to_frame(name="Mean").T

    # Save CV Results Table
    save_df_as_png(
        cv_results_df.round(4),
        f"{output_prefix}_cv_results.png",
    )

    # 4. Final Training & Evaluation
    print("Training final model and evaluating on test set...")
    ridge_pipe.fit(X_train, y_train)
    y_pred = ridge_pipe.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    results_df = pd.DataFrame({"Metric": ["MSE", "R2 Score"], "Value": [mse, r2]})

    print(f"Test MSE: {mse:.4f}")
    print(f"Test R2: {r2:.4f}")

    # Save Test Results Table
    save_df_as_png(results_df.round(4), f"{output_prefix}_test_metrics.png")

    # 5. Visualization (Actual vs Predicted & Residuals)
    # Set plot style
    try:
        import scienceplots

        plt.style.use(["science", "notebook", "grid"])
    except ImportError:
        sns.set_theme(style="whitegrid")

    residuals = y_test - y_pred

    fig = plt.figure(figsize=(14, 6))
    gs = gridspec.GridSpec(1, 2, figure=fig, wspace=0.2)

    # Plot 1: Actual vs Predicted
    min_val = min(y_test.min(), y_pred.min())
    max_val = max(y_test.max(), y_pred.max())

    ax1 = fig.add_subplot(gs[0])
    ax1.scatter(y_test, y_pred, alpha=0.6, edgecolors="k", linewidth=0.5)
    ax1.plot(
        [min_val, max_val], [min_val, max_val], "r--", lw=2, label="Perfect Prediction"
    )
    ax1.set_xlabel("Actual Stress Level", fontsize=12)
    ax1.set_ylabel("Predicted Stress Level", fontsize=12)
    ax1.set_title(
        "Actual vs Predicted Stress Levels", fontsize=14, fontweight="bold", loc="left"
    )
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Plot 2: Residuals
    ax2 = fig.add_subplot(gs[1])
    ax2.scatter(y_pred, residuals, alpha=0.6, edgecolors="k", linewidth=0.5)
    ax2.axhline(y=0, color="r", linestyle="--", lw=2)
    ax2.set_xlabel("Predicted Stress Level", fontsize=12)
    ax2.set_ylabel("Residuals (Actual - Predicted)", fontsize=12)
    ax2.set_title("Residual Plot", fontsize=14, fontweight="bold", loc="left")
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plot_filename = f"{output_prefix}_prediction_plots.png"
    try:
        plt.savefig(plot_filename, bbox_inches="tight")
        print(f"Prediction plots saved to '{plot_filename}'")
    except Exception as e:
        print(f"Error saving plots: {e}")
    finally:
        plt.close(fig)


if __name__ == "__main__":
    run_model()

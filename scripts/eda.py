import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns
from scipy.stats import linregress, gaussian_kde
import numpy as np
import click
import os


@click.command()
@click.option(
    "--input-file",
    default="../data/processed/sleep_data_clean.csv",
    help="Path to the cleaned data file",
)
@click.option("--output-dir", default="results", help="Directory to save the figures")
def perform_eda(input_file, output_dir):
    """
    Performs Exploratory Data Analysis on the training split of the data
    and saves the resulting figures.
    """
    # Load data
    try:
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        return

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Filter for training data if the 'train' column exists
    if "train" in df.columns:
        train_df = df[df["train"] == 1].copy()
        print(f"Using training subset: {len(train_df)} samples.")
    else:
        train_df = df.copy()
        print("Warning: 'train' column not found. Using entire dataset for EDA.")

    # Set plot style
    try:
        import scienceplots

        plt.style.use(["science", "notebook", "grid"])
    except ImportError:
        print("Warning: 'scienceplots' not found. Using default seaborn style.")
        sns.set_theme(style="whitegrid")

    # Custom color palette from notebook
    seshadri = [
        "#c3121e",
        "#0348a1",
        "#ffb01c",
        "#027608",
        "#0193b0",
        "#9c5300",
        "#949c01",
        "#7104b5",
    ]

    # Create figure
    fig = plt.figure(figsize=(15, 12), dpi=100)
    gs = gridspec.GridSpec(2, 2, figure=fig)
    gs.update(wspace=0.21, hspace=0.21)

    # PLOT 1: Sleep Duration vs Stress Level
    ax1 = fig.add_subplot(gs[0])
    # Check if sufficient data for regression
    if len(train_df) > 1:
        lr1 = linregress(y=train_df["sleep_duration"], x=train_df["stress_level"])
        sns.regplot(
            data=train_df,
            x="sleep_duration",
            y="stress_level",
            ci=False,
            line_kws=dict(color=seshadri[0], alpha=0.4),
            scatter_kws=dict(color=seshadri[1]),
            ax=ax1,
        )
        ax1.text(
            0.71,
            0.855,
            f"r : {lr1.rvalue:.3f} \np : {lr1.pvalue:.3e}",
            fontsize=14,
            transform=ax1.transAxes,
            bbox=dict(facecolor="white", edgecolor="black"),
        )
    else:
        sns.scatterplot(data=train_df, x="sleep_duration", y="stress_level", ax=ax1)

    ax1.text(
        0.01,
        1.02,
        "(a)",
        color="red",
        fontsize=20,
        fontweight="bold",
        transform=ax1.transAxes,
    )
    ax1.set_xlabel("Sleep Duration")
    ax1.set_ylabel("Stress Level")

    # PLOT 2: Sleep Quality vs Stress Level
    ax2 = fig.add_subplot(gs[1])
    if len(train_df) > 1:
        lr2 = linregress(y=train_df["sleep_quality"], x=train_df["stress_level"])
        sns.regplot(
            data=train_df,
            x="sleep_quality",
            y="stress_level",
            ci=False,
            line_kws=dict(color=seshadri[0], alpha=0.4),
            scatter_kws=dict(color=seshadri[1]),
            ax=ax2,
        )
        ax2.text(
            0.68,
            0.855,
            f"r : {lr2.rvalue:.3f} \np : {lr2.pvalue:.3e}",
            fontsize=14,
            transform=ax2.transAxes,
            bbox=dict(facecolor="white", edgecolor="black"),
        )
    else:
        sns.scatterplot(data=train_df, x="sleep_quality", y="stress_level", ax=ax2)

    ax2.text(
        0.01,
        1.02,
        "(b)",
        color="red",
        fontsize=20,
        fontweight="bold",
        transform=ax2.transAxes,
    )
    ax2.set_xlabel("Sleep Quality")
    ax2.set_ylabel("Stress Level")

    # PLOT 3: Violin Plot Sleep Disorder vs Stress
    ax3 = fig.add_subplot(gs[2])
    if not train_df.empty:
        sns.violinplot(
            data=train_df,
            y="sleep_disorder",
            x="stress_level",
            hue="sleep_disorder",
            palette=seshadri[: len(train_df["sleep_disorder"].unique())],
            alpha=0.7,
            ax=ax3,
            legend=False,
        )
    ax3.text(
        0.01,
        1.02,
        "(c)",
        color="red",
        fontsize=20,
        fontweight="bold",
        transform=ax3.transAxes,
    )
    ax3.set_ylabel("Sleep Disorder")
    ax3.set_xlabel("Stress Level")

    # PLOT 4: Density Plot of Stress Level
    ax4 = fig.add_subplot(gs[3])
    if len(train_df) > 1 and train_df["stress_level"].nunique() > 1:
        kde = gaussian_kde(train_df["stress_level"])
        x_range = np.linspace(
            train_df["stress_level"].min(), train_df["stress_level"].max(), 200
        )
        y_kde = kde(x_range)
        ax4.plot(x_range, y_kde, color=seshadri[0], linewidth=2.5, alpha=0.8)
        ax4.fill_between(x_range, y_kde, alpha=0.3, color=seshadri[0])
    ax4.set_xlabel("Stress Level")
    ax4.set_ylabel("Density")
    ax4.text(
        0.01,
        1.02,
        "(d)",
        color="red",
        fontsize=20,
        fontweight="bold",
        transform=ax4.transAxes,
    )

    # Save figure
    output_path = os.path.join(output_dir, "eda_summary.png")
    try:
        plt.savefig(output_path, bbox_inches="tight")
        print(f"EDA summary figure saved to '{output_path}'")
    except Exception as e:
        print(f"Error saving figure: {e}")


if __name__ == "__main__":
    perform_eda()

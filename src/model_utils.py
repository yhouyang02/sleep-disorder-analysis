import matplotlib.pyplot as plt


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

"""
eda.py
Module for basic exploratory data analysis.
"""

import pandas as pd
import matplotlib.pyplot as plt


def print_summary(df: pd.DataFrame) -> None:
    """
    Print shape, data types, and descriptive statistics.

    Args:
        df: Cleaned DataFrame.
    """
    print("=== SHAPE ===")
    print(f"{df.shape[0]} rows, {df.shape[1]} columns\n")

    print("=== COLUMN TYPES ===")
    print(df.dtypes)

    print("\n=== FIRST 5 ROWS ===")
    print(df.head())

    print("\n=== STATISTICS ===")
    print(df.describe())


def plot_distributions(df: pd.DataFrame) -> None:
    """
    Plot histograms for all numeric columns and save to file.

    Args:
        df: Cleaned DataFrame.
    """
    num_cols = df.select_dtypes(include="number").columns.tolist()

    if not num_cols:
        print("No numeric columns to plot.")
        return

    num_plots = len(num_cols)
    fig, axes = plt.subplots(1, num_plots, figsize=(5 * num_plots, 4))

    # handle case where there is only one numeric column
    if num_plots == 1:
        axes = [axes]

    for ax, col in zip(axes, num_cols):
        df[col].hist(ax=ax, bins=20, edgecolor="white", color="#5DCAA5")
        ax.set_title(col)
        ax.set_xlabel("value")
        ax.set_ylabel("count")

    plt.suptitle("Numeric Column Distributions", fontsize=13)
    plt.tight_layout()
    plt.savefig("eda_distributions.png", dpi=150)
    print("Plot saved as eda_distributions.png")
    plt.show() 
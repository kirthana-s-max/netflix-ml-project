"""
main.py
Entry point — runs the full Day 1 pipeline:
  1. Load raw data
  2. Clean data
  3. Run EDA
  4. Save cleaned data
"""

from clean import load_data, clean_data, save_data
from eda import print_summary, plot_distributions

# --- file paths ---
RAW_PATH = "netflix_titles.csv"
CLEAN_PATH = "netflix_cleaned.csv"


def main() -> None:
    """Run the full data pipeline."""

    print("\n--- STEP 1: Load ---")
    df = load_data(RAW_PATH)

    print("\n--- STEP 2: Clean ---")
    df = clean_data(df)

    print("\n--- STEP 3: EDA ---")
    print_summary(df)
    plot_distributions(df)

    print("\n--- STEP 4: Save ---")
    save_data(df, CLEAN_PATH)

    print("\nDay 1 complete!")


if __name__ == "__main__":
    main() 
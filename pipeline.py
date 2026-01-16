import os
import pandas as pd
from config import PARTNER_CONFIG
from ingestion import read_partner_file
from transformations import apply_column_mapping, standardize_fields, validate_data


def run_pipeline():
    os.makedirs("output", exist_ok=True)
    final_dfs = []

    for partner, config in PARTNER_CONFIG.items():
        print(f"Processing {partner}...")

        df_raw = read_partner_file(config["file_path"], config["delimiter"])

        df_mapped = apply_column_mapping(df_raw, config["column_mapping"])

        df_standardized = standardize_fields(df_mapped, config["partner_code"])

        df_valid = validate_data(df_standardized)
        final_dfs.append(df_valid)

    final_df = pd.concat(final_dfs, ignore_index=True)
    final_df.to_csv("output/unified_members.csv", index=False)

    print("Pipeline completed successfully.")
    print(final_df)


if __name__ == "__main__":
    run_pipeline()

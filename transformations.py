import pandas as pd
import re
from datetime import datetime


def apply_column_mapping(df, mapping):
    df = df.rename(columns=mapping)
    return df[list(mapping.values())]


def standardize_dob(value):
    if pd.isna(value):
        return None

    for fmt in ("%m/%d/%Y", "%Y-%m-%d"):
        try:
            return datetime.strptime(str(value), fmt).strftime("%Y-%m-%d")
        except ValueError:
            pass

    return None


def standardize_phone(phone):
    if pd.isna(phone):
        return None

    digits = re.sub(r"\D", "", str(phone))
    if len(digits) == 10:
        return f"{digits[:3]}-{digits[3:6]}-{digits[6:]}"
    return None


def standardize_fields(df, partner_code):
    df["first_name"] = df["first_name"].str.title()
    df["last_name"] = df["last_name"].str.title()
    df["email"] = df["email"].str.lower()
    df["dob"] = df["dob"].apply(standardize_dob)
    df["phone"] = df["phone"].apply(standardize_phone)
    df["partner_code"] = partner_code
    return df


def validate_data(df):
    return df[df["external_id"].notna()]

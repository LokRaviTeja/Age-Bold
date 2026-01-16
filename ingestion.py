import pandas as pd


def read_partner_file(file_path, delimiter):
    return pd.read_csv(file_path, delimiter=delimiter)

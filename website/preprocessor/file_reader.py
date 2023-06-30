import pandas as pd
import os
import csv


def get_file_extension(uploaded_file):
    return os.path.splitext(uploaded_file.name)[1]


def get_delimiter(file):
    sample = file.read().decode('utf-8')
    sniffer = csv.Sniffer()
    dialect = sniffer.sniff(sample)
    file.seek(0)    # To reset the pointer to read from the file again.
    return dialect.delimiter


def read_file(file, delimiter: str = ';'):
    file_extension = get_file_extension(file)
    if file_extension != '.csv' and file_extension != '.txt':
        raise ValueError('Invalid file type. Only .csv and .txt files are allowed.')
    else:
        try:
            df = pd.read_csv(file, delimiter=delimiter)
            return df
        except pd.errors.EmptyDataError:
            raise ValueError('No data in the file')


def get_df_head(df: pd.DataFrame, number_of_rows: int = 10):
    df_head = df.head(number_of_rows)
    df_head = df_head.to_dict('index')
    return df_head


def get_df_stats(df: pd.DataFrame):
    stats = df.describe(include='all')
    column_names = df.columns.values
    types_dict = df.dtypes.to_dict()
    return types_dict


def get_file_name_and_size(file):
    file_name = str(file)
    file_size = round(file.size / 1048576, 2)
    return file_name, file_size

import pandas as pd
from django.shortcuts import render
import os
import csv


def get_file_extension(uploaded_file):
    return os.path.splitext(uploaded_file.name)[1]


def get_delimiter(file):
    sample = file.read().decode('utf-8')
    sniffer = csv.Sniffer()
    dialect = sniffer.sniff(sample)
    file.seek(0)    # Make sure to reset the pointer to read from the file again.
    return dialect.delimiter


def read_file(file):
    file_extension = get_file_extension(file)
    if file_extension != '.csv' and file_extension != '.txt':
        raise ValueError('Invalid file type. Only .csv and .txt files are allowed.')
    else:
        try:
            delimiter = get_delimiter(file)
            print(delimiter)
            df = pd.read_csv(file)
            return df
        except pd.errors.EmptyDataError:
            raise ValueError('No data in the file')


def analyse_df(df: pd.DataFrame):
    print(df.head())

    stats = df.describe(include='all')
    column_names = df.columns.values
    types_dict = df.dtypes.to_dict()

    print(types_dict)

    # Print number of rows and columns
    print("\nNumber of rows and columns:")
    print(df.shape)

    # print(stats)

    return df.head(10)




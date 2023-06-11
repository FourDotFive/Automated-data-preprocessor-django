import pandas as pd
from django.shortcuts import render
import os


def get_file_extension(uploaded_file):
    return os.path.splitext(uploaded_file.name)[1]


def read_file(file, delimiter):

    file_extension = get_file_extension(file)
    print(file_extension)
    if file_extension != '.csv' and file_extension != '.txt':
        raise ValueError('Invalid file type. Only .csv and .txt files are allowed.')
    else:
        try:
            df = pd.read_csv(file)
        except pd.errors.EmptyDataError:
            raise ValueError('No data in the file')





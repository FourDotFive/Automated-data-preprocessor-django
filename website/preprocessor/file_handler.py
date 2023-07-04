import datetime
import json
import pandas as pd
import os
import csv
from django.conf import settings


def get_file_name_and_extension(uploaded_file):
    file_name, file_extension = os.path.splitext(uploaded_file.name)
    if file_extension not in ['.csv', '.txt']:
        raise ValueError('Invalid file type. Only .csv and .txt files are allowed.')
    else:
        return file_name, file_extension


def get_delimiter(file):
    file.seek(0)    # To reset the pointer to read from the file again.
    sample = file.read().decode('utf-8')
    sniffer = csv.Sniffer()
    dialect = sniffer.sniff(sample)
    file.seek(0)
    return dialect.delimiter


def read_file(file, delimiter: str = ';'):
    try:
        df = pd.read_csv(file, delimiter=delimiter)
        return df
    except pd.errors.EmptyDataError:
        raise ValueError('No data in the file')


def read_file_from_temp(folder_name):
    folder_dir = os.path.join(settings.MEDIA_ROOT, 'temp', folder_name)
    json_path = os.path.join(folder_dir, 'data.json')

    with open(json_path, 'r') as json_file:
        data = json.load(json_file)

    extension = data['extension']
    delimiter = data['delimiter']

    file_path = os.path.join(folder_dir, 'file' + extension)
    df = pd.read_csv(file_path, delimiter=delimiter)

    return df


def get_df_head_dict(df: pd.DataFrame, number_of_rows: int = 10):
    df_head = df.head(number_of_rows)
    df_head = df_head.to_dict(orient='index')
    return df_head


def get_df_stats(df: pd.DataFrame):
    stats = df.describe(include='all')
    column_names = df.columns.values
    types_dict = df.dtypes.to_dict()
    return types_dict


def get_file_name_and_size(file):
    return round(file.size / 1048576, 2)


def save_file_and_info(file, name, extension, delimiter):
    file.seek(0)
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S-%f")

    folder_name = timestamp + '-' + name

    folder_dir = os.path.join(settings.MEDIA_ROOT, 'temp', folder_name)
    os.makedirs(folder_dir, exist_ok=False)

    json_path = os.path.join(folder_dir, 'data.json')
    file_path = os.path.join(folder_dir, 'file' + extension)

    data = {
        'file_initial_name': name,
        'extension': extension,
        'delimiter': delimiter
    }

    with open(json_path, 'w') as json_file:
        json.dump(data, json_file)

    with open(file_path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    file.seek(0)

    return folder_name

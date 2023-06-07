import pandas as pd
from django.shortcuts import render


def read_file(request):
    try:
        file = request.FILES['file']
        df = pd.read_csv(file)
    except pd.errors.EmptyDataError:
        raise ValueError('No data in the file')



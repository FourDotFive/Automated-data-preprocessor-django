from django.shortcuts import render
from .forms import FileUploadForm
from .data_analysis import read_file, analyse_df, get_delimiter
import json


def file_uploader_view(request):
    if request.method == 'POST':
        file_form = FileUploadForm(request.POST, request.FILES)
        if file_form.is_valid():
            file = request.FILES['file']
            file_name = str(file)
            file_size = round(file.size / 1048576, 2)
            if_detect_delimiter = file_form.cleaned_data.get('if_detect_delimiter')
            if if_detect_delimiter:
                delimiter = get_delimiter(file)
            else:
                delimiter = file_form.cleaned_data['delimiter']
            try:
                df = read_file(file, delimiter)
                df_head = analyse_df(df)
            except ValueError as e:
                return render(request, 'error.html', {'error_message': str(e)})
            else:
                df_html = df_head.to_html()
                context = {
                    'file_name': file_name,
                    'file_size': file_size,
                    'df_html': df_html
                }
                return render(request, 'data_stats.html', context=context)

    file_form = FileUploadForm(request.POST)
    return render(request, 'uploader.html', context={'file_form': file_form})
